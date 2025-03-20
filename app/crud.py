from sqlalchemy.orm import Session
from sqlalchemy import and_
from sqlalchemy.sql import func
from app.models import FactAdMetricsDaily, DimDate, DimRegion, DimPlatform, DimAgeGroup, DimGender, DimPlacement, DimDeviceType
from app.schemas import MetricsFilter

def get_ad_metrics(db: Session, filters: MetricsFilter):
    query = db.query(
        DimDate.date_value.label("date"),
        DimRegion.region_name.label("region"),
        DimPlatform.platform_name.label("platform"),
        DimAgeGroup.age_range.label("age_group"),
        DimGender.gender_name.label("gender"),
        DimPlacement.placement_name.label("placement"),
        DimDeviceType.device_type_name.label("device_type"),
        FactAdMetricsDaily.impressions,
        FactAdMetricsDaily.clicks,
        FactAdMetricsDaily.cost,
        FactAdMetricsDaily.conversions,
        FactAdMetricsDaily.likes
    ).join(DimDate, FactAdMetricsDaily.date_id == DimDate.date_id
    ).join(DimRegion, FactAdMetricsDaily.region_id == DimRegion.region_id
    ).join(DimPlatform, FactAdMetricsDaily.platform_id == DimPlatform.platform_id
    ).join(DimAgeGroup, FactAdMetricsDaily.age_id == DimAgeGroup.age_id
    ).join(DimGender, FactAdMetricsDaily.gender_id == DimGender.gender_id
    ).join(DimPlacement, FactAdMetricsDaily.placement_id == DimPlacement.placement_id
    ).join(DimDeviceType, FactAdMetricsDaily.device_type_id == DimDeviceType.device_type_id)

    filters_to_apply = []

    if filters.start_date:
        start_date = int(filters.start_date.strftime("%Y%m%d"))
        filters_to_apply.append(FactAdMetricsDaily.date_id >= start_date)

    if filters.end_date:
        end_date = int(filters.end_date.strftime("%Y%m%d"))
        filters_to_apply.append(FactAdMetricsDaily.date_id <= end_date)

    if filters.region:
        filters_to_apply.append(func.lower(DimRegion.region_name) == filters.region.lower())  # Case insensitive

    if filters.platform:
        filters_to_apply.append(func.lower(DimPlatform.platform_name) == filters.platform.lower())  # Case insensitive

    if filters_to_apply:
        query = query.filter(and_(*filters_to_apply))

    return query.all()
