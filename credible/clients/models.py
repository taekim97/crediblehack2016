from __future__ import unicode_literals

from django.db import models

# Create your models here.
# field types: BooleanField, CharField(max_length),
# IntegerField(default), DateField

class Profile(models.Model):
    
    clientId = models.IntegerField(null=True)
    externalId = models.IntegerField(null=True)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    middleInitial = models.CharField(max_length=1)
    dateOfBirth = models.DateField()
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    stateAbbreviation = models.CharField(max_length=2)
    zipCode = models.IntegerField(null=True)
    billingLastName = models.CharField(max_length=200)
    billingFirstName = models.CharField(max_length=200)
    billingAddress1 = models.CharField(max_length=200)
    billingAddress2 = models.CharField(max_length=200)
    billingCity = models.CharField(max_length=200)
    billingStateAbbreviation = models.CharField(max_length=2)
    billingZipCode = models.IntegerField(null=True)
    geographicalArea = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    residenceType = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    statusDate = models.DateField()
    homePhone = models.CharField(max_length=200)
    emergencyPhone = models.CharField(max_length=200)
    emergencyContact = models.CharField(max_length=200)
    ssn = models.CharField(max_length=200)
    maritalStatus = models.CharField(max_length=200)
    sex = models.CharField(max_length=200)
    isDeaf = models.BooleanField()
    employeeStatus = models.CharField(max_length=200)
    spouseName = models.CharField(max_length=200)
    referredBy = models.CharField(max_length=200)
    referredNPI = models.CharField(max_length=200)
    referredUPIN = models.CharField(max_length=200)
    referredSource = models.CharField(max_length=200)
    firstSVCDate = models.DateField()
    firstBillSVCDate = models.DateField()
    lastSVCDate = models.DateField()
    lastBillSVCDate = models.DateField()
    referralDate = models.DateField()
    assessmentDate = models.DateField()
    intakeDate = models.DateField()
    admissionDate = models.DateField()
    dischargeDate = models.DateField()
    reportingUnit = models.CharField(max_length=200)
    assignedBenefits = models.CharField(max_length=200)
    releaseInformation = models.CharField(max_length=200)
    signatureSource = models.CharField(max_length=200)
    isGenderRequired = models.BooleanField()
    isHighNoShow = models.BooleanField()
    isDeleted = models.BooleanField()
    liability = models.CharField(max_length=200)
    doNotCall = models.BooleanField()
    severityLevel = models.CharField(max_length=200)
    isLegalGuardianSignatureRequired = models.BooleanField()
    claimNote = models.CharField(max_length=200)
    isFosterparent = models.BooleanField()
    fosterhomeId = models.IntegerField(null=True)
    cisClientId = models.IntegerField(null=True)
    email = models.CharField(max_length=200)
    doNotBillDirect = models.BooleanField()
    sureScriptsFileId = models.IntegerField(null=True)
    caseManagerEmpId = models.IntegerField(null=True)
    raceId = models.IntegerField(null=True)
    ethnicityId = models.IntegerField(null=True)
    raceDescription = models.CharField(max_length=200)
    ethnicityDescription = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    date = models.DateField()

# class Allergies(models.Model):
    


# class Contacts(models.Model):


# class Medications(models.Model):


# class Diagnoses(models.Model):

