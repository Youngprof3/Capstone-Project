from pydantic import BaseModel
class feature(BaseModel):
    Year: int
    Month: int
    Day: int
    Extended: int
    Suicide: int
    Attack_Group: int
    No_Of_Killed: int
    No_Of_Wounded: float
    Property: int
    country: int
    region: int
    attacktype1: int
    targtype1: int
    natlty1: float
    weaptype1: int
    