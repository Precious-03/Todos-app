Ranking = []

while True:
    Request = input("add name,Change rank,see,end:")
    Request = Request.strip()

    match Request:
      case "add name":
        Ranking_new= input("name:")
        Ranking.append(Ranking_new)
      case "Change rank":
        Ranking_change = input("State the rank: ")
        Ranking_name = input("Enter new name:")
        Ranking[int(Ranking_change) - 1] = Ranking_name
      case "see":
          for i in Ranking:
            print(i)
      case "end":
          break






