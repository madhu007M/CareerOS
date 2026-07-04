"""
Company Repository
"""

from sqlalchemy.orm import Session

from backend.app.models.company import Company


class CompanyRepository:

    def get_or_create(self, db: Session, name: str):

        company = (
            db.query(Company)
            .filter(Company.name == name)
            .first()
        )

        if company:
            return company

        company = Company(
            name=name
        )

        db.add(company)
        db.commit()
        db.refresh(company)

        return company


company_repository = CompanyRepository()