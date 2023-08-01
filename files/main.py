import sentry_sdk

sentry_sdk.init(
    dsn="https://c6be3e623f7d624d80eab49ee3ba7d18@o4505628062056448.ingest.sentry.io/4505628187820032",
    environment="development",
    release="1.0"
  # Set traces_sample_rate to 1.0 to capture 100%
  # of transactions for performance monitoring.
  # We recommend adjusting this value in production.
  #traces_sample_rate=1.0
)

if __name__ == "__main__":
    devision_zero = 1 /0