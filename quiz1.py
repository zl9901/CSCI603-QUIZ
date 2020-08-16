import turtle





def main():
    radius = 50
    for i in range(3):
        turtle.circle(radius)
        if i < 2:
            turtle.forward(radius * 2)
    turtle.done()


if __name__ == "__main__":
	main()