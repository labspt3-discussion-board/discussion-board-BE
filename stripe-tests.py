import stripe
import os

# Set your secret key: remember to change this to your live secret key in production
# See your keys here: https://dashboard.stripe.com/account/apikeys
stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

charge = stripe.Charge.create(
  amount=999,
  currency='usd',
  source='tok_visa',
  receipt_email='jenny.rosen@example.com',
)

print(charge)
