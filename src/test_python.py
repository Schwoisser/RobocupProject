import argparse


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--song", type=str, help="Patho to Song")
	parser.add_argument("--car", type=str, help="character")
	args = parser.parse_args()
	#parser.add_argument("--ip", type=str, default="nao5.local", help="Robot ip address")
	#parser.add_argument("--port", type=int, default=9559, help="Robot port number")
	print args.song
	print args.car
	args = parser.parse_args()