import requests
from bs4 import BeautifulSoup
import urllib
import base64
import re
import shutil
import os

class DecodeURL:
    def __init__(self):
        pass

    def SqmOaLsKHv7vWtli(self, value):
        return value

    def bMGyx71TzQLfdonN(self, value):
        chunks = []
        for i in range(0, len(value), 3):
            chunks.append(value[i:i+3])

        chunks.reverse()
        return ''.join(chunks)

    def Iry9MQXnLs(self, encoded):
        key = "pWB9V)[*4I`nJpp?ozyB~dbr9yt!_n4u"
        decoded = ""
        hex_values = ''.join([bytes.fromhex(char).decode("ASCII") for char in re.findall(r".{1,2}", encoded)])
        for i in range(len(hex_values)):
            decoded += chr(ord(hex_values[i]) ^ ord(key[i % len(key)]))

        adjusted = ""
        for char in decoded:
            adjusted += chr(ord(char) - 3)

        return base64.b64decode(adjusted).decode('latin1')

    def IGLImMhWrI(self, encoded):
        reversed_str = encoded[::-1]
        decoded_str = ''.join([
            chr(ord(c) + 13) if c.islower() and c < 'n' or c.isupper() and c < 'N' else chr(ord(c) - 13) if c.isalpha() else c
            for c in reversed_str
        ])
        return base64.b64decode(decoded_str[::-1]).decode('latin1')

    def GTAxQyTyBx(self, encoded):
        reversed_str = encoded[::-1]
        filtered = ""
        for i in range(0, len(reversed_str), 2):
            filtered += reversed_str[i]
        return base64.b64decode(filtered).decode('latin1')

    def C66jPHx8qu(self, encoded):
        reversed_str = encoded[::-1]
        hex_values = ''.join([bytes.fromhex(char).decode("ASCII") for char in re.findall(r".{1,2}", reversed_str)])
        key = "X9a(O;FMV2-7VO5x;Ao\x05:dN1NoFs?j,"
        decoded_str = ""
        for i in range(len(hex_values)):
            decoded_str += chr(ord(hex_values[i]) ^ ord(key[i % len(key)]))
        return decoded_str

    def MyL1IRSfHe(self, encoded):
        reversed_str = encoded[::-1]
        adjusted = "".join([chr(ord(c) - 1) for c in reversed_str])
        result = ""
        for i in range(0, len(adjusted), 2):
            result += chr(int(adjusted[i:i+2], 16))
        return result

    def detdj7JHiK(self, encoded):
        extracted = encoded[10:-16]
        key = '3SAY~#%Y(V%>5d/Yg"$G[Lh1rK4a;7ok'
        decoded = base64.b64decode(extracted).decode('latin1')
        extended_key = (key * ((len(decoded) + len(key) - 1) // len(key)))[:len(decoded)]
        result = ""
        for i in range(len(decoded)):
            result += chr(ord(decoded[i]) ^ ord(extended_key[i]))
        return result

    def nZlUnj2VSo(self, encoded):
        mapping = {
            "x": "a", "y": "b", "z": "c", "a": "d", "b": "e", "c": "f", "d": "g",
            "e": "h", "f": "i", "g": "j", "h": "k", "i": "l", "j": "m", "k": "n",
            "l": "o", "m": "p", "n": "q", "o": "r", "p": "s", "q": "t", "r": "u",
            "s": "v", "t": "w", "u": "x", "v": "y", "w": "z", "X": "A", "Y": "B",
            "Z": "C", "A": "D", "B": "E", "C": "F", "D": "G", "E": "H", "F": "I",
            "G": "J", "H": "K", "I": "L", "J": "M", "K": "N", "L": "O", "M": "P",
            "N": "Q", "O": "R", "P": "S", "Q": "T", "R": "U", "S": "V", "T": "W",
            "U": "X", "V": "Y", "W": "Z"
        }
        return ''.join([mapping[c] if c in mapping else c for c in encoded])

    def laM1dAi3vO(self, encoded):
        reversed_str = encoded[::-1]
        decoded_str = reversed_str.replace('-', '+').replace('_', '/')
        decoded_value = base64.b64decode(decoded_str).decode('latin1')
        result = ""
        for char in decoded_value:
            result += chr(ord(char) - 5)
        return result

    def GuxKGDsA2T(self, encoded):
        reversed_str = encoded[::-1]
        decoded_str = reversed_str.replace('-', '+').replace('_', '/')
        decoded_value = base64.b64decode(decoded_str).decode('latin1')
        result = ""
        for char in decoded_value:
            result += chr(ord(char) - 7)
        return result

    def LXVUMCoAHJ(self, encoded):
        reversed_str = encoded[::-1]
        decoded_str = reversed_str.replace('-', '+').replace('_', '/')
        decoded_value = base64.b64decode(decoded_str).decode('latin1')
        result = ""
        for char in decoded_value:
            result += chr(ord(char) - 3)
        return result

class VidSRC_Resolver:
    def __init__(self, media_type, tmdb_id, season=None, episode=None, verbosity=True):
        self.base_url = "https://vidsrc.net"
        self.verbosity = verbosity
        self.type = media_type
        self.tmdb_id = tmdb_id
        self.season = season
        self.episode = episode
        self.vidsrc_url = self.__build_vidsrc_url()

    def __build_vidsrc_url(self):
        if self.type == "movie":
            return f"{self.base_url}/embed/{self.type}?tmdb={self.tmdb_id}"
        elif self.type == "tv":
            return f"{self.base_url}/embed/{self.type}?tmdb={self.tmdb_id}&season={self.season}&episode={self.episode}"
        else:
            if self.verbosity:
                print("Invalid media type")
            return None
    
    def get_stream(self):
        self.domain, rcp_url = self.__get_rcp()
        prorcp_url = self.__get_prorcp(self.domain, rcp_url)
        self.stream_url = self.__get_stream_url(self.domain, prorcp_url)
        return self.stream_url

    def __get_rcp(self):
        if self.verbosity:
            print(f"[*] Requesting URL: {self.vidsrc_url}")
        resp = requests.post(url=self.vidsrc_url)
        if resp.status_code == 200:
            if self.verbosity:
                print("[+] Successfully Fetched URL")
        else:
            if self.verbosity:
                print(f"[-] Error Fetching URL -> {str(resp.status_code)}")
            return None
        
        if self.verbosity:
            print("[*] Extracting /rcp URL")
        soup = BeautifulSoup(resp.text, 'html.parser')
        iframe = soup.find('iframe', {'id': 'player_iframe'})
        src = iframe.get('src')
        if src.startswith("//"):
            src = "https:" + src
        parsed_url = urllib.parse.urlparse(src)
        domain = parsed_url.netloc
        rcp_endpoint = parsed_url.path
        if self.verbosity:
            print("[*] Extracted rcp and domain")
        return domain, rcp_endpoint

    def __get_prorcp(self, domain, rcp):
        if self.verbosity:
            print(f"[*] Requesting /rcp")
        resp = requests.post(f"http://{domain}{rcp}")
        if resp.status_code == 200:
            if self.verbosity:
                print("[+] Successfully Fetched URL")
        else:
            if self.verbosity:
                print(f"[-] Error Fetching URL -> {str(resp.status_code)}")
            return None
        
        if self.verbosity:
            print("[*] Extracting /prorcp URL")
        matches = re.search(r"src: '(/prorcp[^']*)'", resp.text)
        prorcp_url = matches.group(1) if matches else None
        if prorcp_url:
            if self.verbosity:
                print("[+] Extracted /prorcp")
            return prorcp_url
        else:
            if self.verbosity:
                print("[-] Couldn't Find /prorcp")
            return None

    def __get_stream_url(self, domain, prorcp):
        if self.verbosity:
            print(f"[*] Requesting /prorcp")
        resp = requests.get(f"http://{domain}{prorcp}", headers={"Referer": f"http://{domain}/", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/117.0", "Referrer-Policy": "origin", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "no-cors"})
        if resp.status_code == 200:
            if self.verbosity:
                print("[+] Successfully Fetched URL")
        else:
            if self.verbosity:
                print(f"[-] Error Fetching URL -> {str(resp.status_code)}")
            return None
        
        if self.verbosity:
            print("[*] Extracting Stream URL")
        soup = BeautifulSoup(resp.text, 'html.parser')
        cpt_script = soup.find('script', src=lambda x: x and 'cpt.js' in x)
        decode_js_tag = cpt_script.find_previous('script') if cpt_script else None
        decode_js_script = decode_js_tag['src'] if decode_js_tag else None
        if decode_js_script:
            if self.verbosity:
                print("[+] Found Decode Script")
        else:
            if self.verbosity:
                print("[-] Error Finding Decode Script")
            return None
        
        if self.verbosity:
            print("[*] Fetching Decode Script")
        resp2 = requests.get(f"http://{domain}{decode_js_script}", headers={"Referer": f"http://{domain}/", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/117.0", "Referrer-Policy": "origin", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "no-cors"})
        if resp2.status_code == 200:
            if self.verbosity:
                print("[+] Fetched Decode script")
            decode_script_source = resp2.text
        else:
            if self.verbosity:
                print("[-] Error fetching decode script -> {str(resp2.status_code)}")
            return None
        
        if self.verbosity:
            print("[*] Getting ID & Function")
        pattern = r'{}\}window\[([^"]+)\("([^"]+)"\)'
        matches = re.search(pattern, decode_script_source)
        if matches:
            decode_matches = [matches.group(1), matches.group(2)]
            if self.verbosity:
                print(f"[+] Matches found -> {decode_matches}")
        else:
            if self.verbosity:
                print("[-] No Matches found")
            return None

        element_id = eval(f'DecodeURL().{decode_matches[0]}("{decode_matches[1]}")')
        if element_id:
            if self.verbosity:
                print(f"[+] Found Element ID -> {element_id}")
        else:
            if self.verbosity:
                print("[-] Element ID Not Found")
            return None

        encoded_stream_url = soup.find(id=element_id).text
        if self.verbosity:
            print("[*] Extracted Encoded URL")
            print("[*] Decoding URL")
        stream_url = eval(f'DecodeURL().{decode_matches[1]}("{encoded_stream_url}")')
        if self.verbosity:
            print("[*] Decoded Stream URL")
        return stream_url

    def play_stream(self):
        if self.__check_mpv():
            if self.verbosity:
                print("[*] Launching MPV Player")
            os.system(f'mpv --http-header-fields="Referer: https://{self.domain}/, User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/117.0" "{self.stream_url}"')
        else:
            if self.verbosity:
                print("[-] MPV Player not found, cannot play stream")
    
    def __check_mpv(self):
        if os.name == 'nt':
            return shutil.which("mpv.exe") is not None
        elif os.name == 'posix':
            return shutil.which("mpv") is not None
        else:
            return False
        
resolver = VidSRC_Resolver(media_type="movie", tmdb_id="140607", verbosity=True)
stream = resolver.get_stream()
print(stream)
resolver.play_stream()