from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship
from .database import Base

# Dimension Tables
class DimDate(Base):
    __tablename__ = "dim_date"
    date_id = Column(Integer, primary_key=True, index=True)
    date_value = Column(Date, nullable=False)

class DimRegion(Base):
    __tablename__ = "dim_region"
    region_id = Column(Integer, primary_key=True, index=True)
    region_name = Column(String, nullable=False, unique=True)

class DimAgeGroup(Base):
    __tablename__ = "dim_age_group"
    age_id = Column(Integer, primary_key=True, index=True)
    age_range = Column(String, nullable=False)

class DimGender(Base):
    __tablename__ = "dim_gender"
    gender_id = Column(Integer, primary_key=True, index=True)
    gender_name = Column(String, nullable=False)

class DimPlatform(Base):
    __tablename__ = "dim_platform"
    platform_id = Column(Integer, primary_key=True, index=True)
    platform_name = Column(String, nullable=False, unique=True)

class DimPlacement(Base):
    __tablename__ = "dim_placement"
    placement_id = Column(Integer, primary_key=True, index=True)
    placement_name = Column(String, nullable=False)

class DimDeviceType(Base):
    __tablename__ = "dim_device_type"
    device_type_id = Column(Integer, primary_key=True, index=True)
    device_type_name = Column(String, nullable=False)

# Fact Table for Stores Daily Ad Metrics
class FactAdMetricsDaily(Base):
    __tablename__ = "fact_ad_metrics_daily"

    id = Column(Integer, primary_key=True, index=True)
    date_id = Column(Integer, ForeignKey("dim_date.date_id"), nullable=False)
    region_id = Column(Integer, ForeignKey("dim_region.region_id"), nullable=False)
    age_id = Column(Integer, ForeignKey("dim_age_group.age_id"), nullable=False)
    gender_id = Column(Integer, ForeignKey("dim_gender.gender_id"), nullable=False)
    platform_id = Column(Integer, ForeignKey("dim_platform.platform_id"), nullable=False)
    placement_id = Column(Integer, ForeignKey("dim_placement.placement_id"), nullable=False)
    device_type_id = Column(Integer, ForeignKey("dim_device_type.device_type_id"), nullable=False)
    impressions = Column(Integer, nullable=False)
    clicks = Column(Integer, nullable=False)
    cost = Column(Float, nullable=False)
    conversions = Column(Integer, nullable=False)
    likes = Column(Integer, nullable=False)

    date = relationship("DimDate")
    region = relationship("DimRegion")
    age_group = relationship("DimAgeGroup")
    gender = relationship("DimGender")
    platform = relationship("DimPlatform")
    placement = relationship("DimPlacement")
    device_type = relationship("DimDeviceType")
