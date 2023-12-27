from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class Document(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str
    section_name: Optional[str] = None
    title: Optional[str] = None
    authors: Optional[str] = None
    intro: Optional[str] = None
    url: Optional[str] = Field(default=None, sa_column_kwargs={"unique": True})
    tags: Optional[str] = None
    issue_id: Optional[int] = Field(default=None, foreign_key="issues.id")
    tokens: list["Token"] = Relationship(back_populates="document")


class Issue(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: Optional[str] = None
    year: Optional[int] = None
    number: Optional[int] = None
    issue_url: Optional[str] = Field(
        default=None, sa_column_kwargs={"unique": True})
    issue_cover_url: Optional[str] = None
    documents: list[Document] = Relationship(back_populates="issue")


class Token(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    doc_id: Optional[int] = Field(default=None, foreign_key="documents.id")
    text: str
    lemma: Optional[str] = None
    pos: Optional[str] = None
    tag: Optional[str] = None
    morph_feats: Optional[str] = None
    extended_tag: Optional[str] = None
    dep: Optional[str] = None
    head: Optional[str] = None
    is_alpha: Optional[int] = None
    is_stop: Optional[int] = None
    document: Document = Relationship(back_populates="tokens")
