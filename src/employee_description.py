from typing import Optional
from pydantic import BaseModel


class EmployeeData(BaseModel):
    Age: Optional[int]
    BusinessTravel: Optional[str]
    DailyRate: Optional[int]
    Department: Optional[str]
    DistanceFromHome: Optional[int]
    Education: Optional[int]
    EducationField: Optional[str]
    EmployeeNumber: Optional[int]
    EnvironmentSatisfaction: Optional[int]
    Gender: Optional[str]
    HourlyRate: Optional[int]
    JobInvolvement: Optional[int]
    JobLevel: Optional[int]
    JobRole: Optional[str]
    JobSatisfaction: Optional[int]
    MaritalStatus: Optional[str]
    MonthlyIncome: Optional[int]
    MonthlyRate: Optional[int]
    NumCompaniesWorked: Optional[int]
    OverTime: Optional[str]
    PercentSalaryHike: Optional[int]
    PerformanceRating: Optional[int]
    RelationshipSatisfaction: Optional[int]
    StockOptionLevel: Optional[int]
    TotalWorkingYears: Optional[int]
    TrainingTimesLastYear: Optional[int]
    WorkLifeBalance: Optional[int]
    YearsAtCompany: Optional[int]
    YearsInCurrentRole: Optional[int]
    YearsSinceLastPromotion: Optional[int]
    YearsWithCurrManager: Optional[int]


class EmployeeResponse(BaseModel):
    probability: float
    attrition: int
