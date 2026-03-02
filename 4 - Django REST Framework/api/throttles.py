from rest_framework.throttling import UserRateThrottle

class BurstUserRateThrottle(UserRateThrottle):
    scope = 'burst'

class SustainedRateThrottle(UserRateThrottle):
    scope = 'sustained'