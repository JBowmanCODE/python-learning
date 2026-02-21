films = ["Batman", "Pulp Fiction", "Res Dogs", "Star Wars", "Star Wars 2"]

# Print each film using a loop
for film in films:
    print(film)  # film not films

# Add a new film
films.append("Ghostbusters")

# Remove your least favourite
films.remove("Batman")

# Print final list and count
print(films)
print(f"I have {len(films)} films in my list.")