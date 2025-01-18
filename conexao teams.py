import win32com.client

# conectar ao outlook
outlook = win32com.client.Dispatch("Outlook.Aplication")
namespace = outlook.GetNamespace("MAPI")