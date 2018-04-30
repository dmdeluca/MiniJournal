import datetime
import os

def get_io():
	entry_text = ""
	options = {'save':'s','quit':'q'}
	print("  "+options['save']+" - save\n  "+options['quit']+" - quit\n-----")
	while True:	
		new_line = input('\t>> ')
		if new_line == 's':
			now = datetime.datetime.now()
			now_text = now.strftime("%Y-%m-%d-%H-%M")
			file_name = now_text + ".txt"
			try:
				with open(os.path.join("entries",file_name),'w') as my_file:
					print('Journal Entry from '+now.strftime("%A, %B %d, %Y at %I:%M%p")+entry_text+'\n[End of entry.]',file=my_file)
					my_file.close()
				print("Entry saved as "+file_name+".")
				break
			except:
				print("Error saving file.")
				print("Returned to editor.")
				print(entry_text)
		elif new_line == 'q':
			print("Closed entry without saving.\nReturned to main menu.")
			break
		else:
			entry_text += '\n  '+new_line

def open_entry():
	while True:
		file_list = os.listdir('entries')
		if len(file_list) > 0:
			for c,i in enumerate(file_list,1):
				print(str(c)+". "+i)
			while True:
				file_number = abs(int(input("Enter number: ")))
				#print("length of list: "+str(len(file_list)))
				#print("file number given: "+str(file_number))
				if file_number <= len(file_list):
					break
				else:
					print("Invalid number.")
			try:
				with open(os.path.join('entries',file_list[file_number-1]),'r') as file:
					file_text = file.read()
					print("-----\n"+file_text+"-----")
			except:
				print("Error opening file.")
			finally:
				break
		else:
			print("There are no entries to read.")
			break

def get_options():
	print("Welcome to mini journal.")
	if not os.path.exists('entries'):
		os.makedirs('entries')
	options = {'quit':'q','read':'r','new':'n'}
	while True:
		print("  "+options['read']+" - read an existing entry")
		print("  "+options['new']+" - write a new entry")
		print("  "+options['quit']+" - quit the program")
		user_input = input(">> ")
		if user_input == options['read']:
			open_entry()
		elif user_input == options['quit']:
			input("Bye!")
			break
		elif user_input == options['new']:
			get_io()
		else:
			print("Invalid command.")

def main_loop():
	get_options()
	quit()

main_loop()