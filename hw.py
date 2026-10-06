temperature = float(input("Enter the current temperature in °C: "))

if temperature > 25:
  print("It is warm! You can wear light and soft clothes.")
elif temperature >= 15 and temperature <= 25:
  print("The weather is pleasant. A light shirt or t-shirt is fine.")
else:
  print("It is cold outside! You should wear a jacket or pullover.")
