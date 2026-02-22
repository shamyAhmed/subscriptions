from datetime import datetime, timezone;
from sqlalchemy.orm import Mapped, mapped_column;

current_date = lambda: datetime.now(timezone.utc);
class BaseTimestamp():
    created_at: Mapped[datetime] = mapped_column(init=False, default=current_date);
    updated_at: Mapped[datetime] = mapped_column(init=False, onupdate=current_date, default=current_date)