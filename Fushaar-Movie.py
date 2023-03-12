from requests import get
import re,os
def header():
    os.system('cls' if os.name=='nt' else 'clear');print("""
███████╗██╗   ██╗███████╗██╗  ██╗ █████╗ ██████╗       ███╗   ███╗ ██████╗ ██╗   ██╗██╗███████╗
██╔════╝██║   ██║██╔════╝██║  ██║██╔══██╗██╔══██╗      ████╗ ████║██╔═══██╗██║   ██║██║██╔════╝
█████╗  ██║   ██║███████╗███████║███████║██████╔╝█████╗██╔████╔██║██║   ██║██║   ██║██║█████╗  
██╔══╝  ██║   ██║╚════██║██╔══██║██╔══██║██╔══██╗╚════╝██║╚██╔╝██║██║   ██║╚██╗ ██╔╝██║██╔══╝  
██║     ╚██████╔╝███████║██║  ██║██║  ██║██║  ██║      ██║ ╚═╝ ██║╚██████╔╝ ╚████╔╝ ██║███████╗
╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝      ╚═╝     ╚═╝ ╚═════╝   ╚═══╝  ╚═╝╚══════╝                                                                                   
                                                                                                       
                                By @TweakPY - @vv1ck
""")  
header()
movie_name=str(input('- The Movie Name : ')).replace(' ','-')# Like : the system 
req=get(f'https://www.fushaar.com/movie/{movie_name}',headers={'referer': 'https://www.fushaar.com/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}).text
try:header();movie_url=re.findall('<a class="watch-hd" href="(.*?)" target="_blank" download>تحميل مباشر جوده 1080/FullHD </a>',req)[0]
except:print('- Movie Not Found ');exit()
try:description=re.findall('<meta property="og:description" content="(.*?)" />',req)[0]
except:description=''
print(f"- URL : {movie_url}\n\n- Description : {description}\n")