import csv
import os


CLIENT_TABLE = ".clients.csv"
CLIENT_SCHEMA = ["name", "company", "email","position"]
clients = []

def _initialize_clients_from_storage():
   with open(CLIENT_TABLE, mode = "r") as f:
      reader = csv.DictReader(f, fieldnames= CLIENT_SCHEMA)

      for row in reader:
         clients.append(row)

def _save_clients_to_storage():
   tmp_table_name = "{}.tmp".format(CLIENT_TABLE)
   with open(tmp_table_name, mode="w") as f:
      writer = csv.DictWriter(f, fieldnames = CLIENT_SCHEMA)
      writer.writerows(clients)

      os.remove(CLIENT_TABLE)
      os.rename(tmp_table_name, CLIENT_TABLE)



def create_client(client_name):
    global clients
    
    if client_name not in clients:
       clients.append(client_name)
       
    else:
       print("Client already is in the client\'s list") 

   # _add_comma()

def list_clients():
   for idx, client in enumerate(clients):
      print("{uid}, {name}, {company}, {email}, {position}".format(
         uid=idx,
         name=client["name"],
         company=client["company"],
         email=client["email"],
         position=client["position"],))

   print(clients)


"""def update_client(client_name, updated_client_name):
   global clients
   
   if client_name in clients:
      index = clients.index(client_name)
      clients[index] = update_client
   else:
      print("Client is not in clients list")"""

def update_client(client_name, updated_client_name):
    global clients

    for client in clients:
        if client["name"] == client_name:
            client["name"] = updated_client_name  # Cambia solo el nombre del cliente
            print("Client updated successfully!")
            return
    
    print("Client is not in clients list")

def delete_client(client_name):
   global clients

   if client_name in clients:
      clients.remove(client_name)
   else:
      print("Client is not in clients list")


def search_client(client_name):
   for client in clients:
      if client != client_name:
         continue
      else:
         return True


def _print_welcome():
   print("WELCOME TO PLATZI VENTAS")
   print("*" * 50)
   print("What would you like to do today?")
   print("[C]reate client")
   print("[L]ist client")
   print("[U]pdate client")
   print("[D]elete client")
   print("[S]earch client")


def _get_client_field (field_name):
   field = None

   while not field:
      field = input ("What is the client {}?".format(field_name))

      return field


def _get_client_name():
   client_name = None

   while not client_name:
      client_name = input ("What is the client name?")

      if client_name == "exit":
         client_name = None
         break

   if not client_name:
         sys.exit()

   return client_name

if __name__ == "__main__":
  _initialize_clients_from_storage()

  _print_welcome()
  
  command = input()
  command = command.upper()

  if command == "C":
      client = {
         "name" : _get_client_field("name"),
         "company" : _get_client_field("company"),
         "email" : _get_client_field("email"),
         "position" : _get_client_field("position"),
      }
      create_client(client)

  elif command == "L":
      list_clients()
  elif command == "D":
     client_name = _get_client_name()
     delete_client(client_name)
  elif command == "U":
     client_name = _get_client_name()
     updated_client_name = input ("What is the new client name")
     update_client(client_name, updated_client_name)
   
  elif command == "S":
      client_name = _get_client_name()
      found = search_client (client_name)
  

      if found:
         print("The client is in the client\'s list")
      else:
         print("The client:{}is not in our client\'s".format(client_name)) 
  else:
     print("Invalid command")
     
_save_clients_to_storage()




