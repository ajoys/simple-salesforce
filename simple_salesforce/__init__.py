"""Simple-Salesforce Package"""

from simple_salesforce.api import (
    Salesforce,
    SalesforceAPI,
    SFType,
    SalesforceMoreThanOneRecord,
    SalesforceExpiredSession,
    SalesforceRefusedRequest,
    SalesforceResourceNotFound,
    SalesforceGeneralError,
    SalesforceMalformedRequest
)

from simple_salesforce.login import (
    SalesforceLogin, SalesforceAuthenticationFailed
)
