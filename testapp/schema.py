# schema.py
import graphene
from graphene_django.types import DjangoObjectType
from .models import Company, Department, Employee
from .tasks import generate_company_report


class CompanyType(DjangoObjectType):
    class Meta:
        model = Company

class DepartmentType(DjangoObjectType):
    class Meta:
        model = Department

class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee

class Query(graphene.ObjectType):
    all_companies = graphene.List(CompanyType)
    company_by_id = graphene.Field(CompanyType, id=graphene.Int(required=True))

    def resolve_all_companies(self, info):
        return Company.objects.all()

    def resolve_company_by_id(self, info, id):
        return Company.objects.get(id=id)


class GenerateReportMutation(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        company_id = graphene.Int(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, company_id, email):
        print("-------------geber")
        generate_company_report.delay(company_id, email)  # Trigger the Celery task
        return GenerateReportMutation(success=True)

class Mutation(graphene.ObjectType):
    generate_report = GenerateReportMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)



