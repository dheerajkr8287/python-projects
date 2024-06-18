
import phonenumbers
from phonenumbers import timezone, geocoder, carrier

def get_phone_number_info():
    number = input("Enter your phone number with country code (e.g., +1 for US): ")
    try:
        phone = phonenumbers.parse(number)
        time_zones = timezone.time_zones_for_number(phone)
        carrier_name = carrier.name_for_number(phone, "en")
        region = geocoder.description_for_number(phone, "en")

        print(f"Phone Number: {number}")
        print(f"Parsed: {phone}")
        print(f"Time Zones: {time_zones}")
        print(f"Carrier: {carrier_name}")
        print(f"Region: {region}")

    except phonenumbers.NumberParseException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_phone_number_info()
