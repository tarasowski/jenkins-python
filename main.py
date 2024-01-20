def main():
  return "hello world"

def handler(event, ctx):
  return event

print(
  main(),
  "from my push",
  handler({"message": "this is my jenkins test"}, None)
)
