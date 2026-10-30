from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class TextEntry(Base):
    __tablename__ = "textmap"
    
    id: Mapped[str] = mapped_column(primary_key=True)
    en: Mapped[str]
    chs: Mapped[str]
    version: Mapped[str]
    text_source: Mapped[str]
    

    