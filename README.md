#CheckerMailPy

## How to install:
	git clone https://github.com/dark0ghost/CheckerMailPy.git
  
  
## How to use (sync):
     
         import CheckerMailPy
         from email.mime.text import MIMEText
         
         def sync_start() -> None:
           checker_mail: CheckerEmail.CheckerEmail = CheckerEmail.CheckerEmail(hostname_mail=smtp_host,
                                                                    port=smtp_port, password=smtp_password,
                                                                    login=smtp_login)
           check.change_len_code(new_len_code=5)
           check.get_random_code()
           code: int = check.get_code()
           check.sync_send_message()
           
## How to use (async):
            from CheckerMailPy import CheckerEmail
            from email.mime.text import MIMEText
            
            async def async_start() -> None:
                checker_mail: CheckerEmail.CheckerEmail = CheckerEmail.CheckerEmail(hostname_mail=smtp_host,
                                                                    port=smtp_port, password=smtp_password,
                                                                    login=smtp_login)
                check.change_len_code(new_len_code=5)
                check.get_random_code()
                code: int = check.get_code()
                await check.async_send_message()
                
