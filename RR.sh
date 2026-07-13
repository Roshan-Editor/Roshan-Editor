#!/bin/bash
clear

# फोल्डर स्ट्रक्चर सेटिंग्स
mkdir -p $HOME/.RR
mkdir -p $HOME/.RR-simu
mkdir -p $HOME/.toolx

# Color Setup
r='\033[1;91m'
p='\033[1;95m'
y='\033[1;93m'
g='\033[1;92m'
n='\033[1;0m'
b='\033[1;94m'
c='\033[1;96m'

# Symbol Setup
X='\033[1;92m[\033[1;00m\u23cf\uae3b\ud83e\udd8a\033[1;92m]\033[1;96m'
D='\033[1;92m[\033[1;00m\u3004\033[1;92m]\033[1;93m'
E='\033[1;92m[\033[1;00m\u00d7\033[1;92m]\033[1;91m'
A='\033[1;92m[\033[1;00m+\033[1;92m]\033[1;92m'
C='\033[1;92m[\033[1;00m</>\033[1;92m]\033[92m'
lm='\033[96m▱▱▱▱▱▱▱▱▱▱▱▱\033[0m〄\033[96m▱▱▱▱▱▱▱▱▱▱▱▱\033[1;00m'
dm='\033[93m▱▱▱▱▱▱▱▱▱▱▱▱\033[0m〄\033[93m▱▱▱▱▱▱▱▱▱▱▱▱\033[1;00m'

# Icon Setup
OS="\uf6a6"
HOST="\uf6c3"
KER="\uf83c"
UPT="\uf49b"
PKGS="\uf8d6"
SH="\ue7a2"
TERMINAL="\uf489"
CHIP="\uf2db"
CPUI="\ue266"
HOMES="\uf015"

# Device Detection
if command -v getprop &>/dev/null; then
    MODEL=$(getprop ro.product.model)
    VENDOR=$(getprop ro.product.manufacturer)
else
    MODEL=$(uname -n)
    VENDOR=$(uname -s)
fi
devicename="${VENDOR} ${MODEL}"
THRESHOLD=100
random_number=$(( RANDOM % 2 ))

exit_script() {
    clear
    echo
    echo
    echo -e ""
    echo -e "${c}              (\_/)"
    echo -e "              (${y}^_^${c})     ${A} ${g}Hey dear${c}"
    echo -e "             ⊂(___)づ  ⋅˚₊‧ ଳ ‧₊˚ ⋅"
    echo -e "\n ${g}[${n}${KER}${g}] ${c}Exiting ${g}RR Banner \033[1;36m"
    echo
    cd "$HOME"
    kill -9 $PPID 2>/dev/null
    exit 0
}

if command -v tput &>/dev/null; then
    echo ""
else
    echo -e " ${C} ${g}Waiting for setup Screen!¡${n}"
    if [ -d "/data/data/com.termux/files/usr/" ]; then
        pkg install ncurses-utils -y >/dev/null 2>&1
    else
        sudo apt install ncurses-bin -y >/dev/null 2>&1 || true
    fi
    clear
fi

if command -v curl &>/dev/null; then
    echo ""
else
    if [ -d "/data/data/com.termux/files/usr/" ]; then
        pkg install curl -y >/dev/null 2>&1
    else
        sudo apt install curl -y >/dev/null 2>&1 || true
    fi
    clear
fi

trap exit_script SIGINT SIGTSTP

check_disk_usage() {
    local threshold=${1:-$THRESHOLD}
    local total_size=$(df -h "$HOME" | awk 'NR==2 {print $2}')
    local used_size=$(df -h "$HOME" | awk 'NR==2 {print $3}')
    local disk_usage=$(df "$HOME" | awk 'NR==2 {print $5}' | sed 's/%//g')

    if [ "$disk_usage" -ge "$threshold" ]; then
        echo -e "${g}[${n}\uf0a0${g}] ${r}WARN: ${y}Disk Full ${g}${disk_usage}% ${c}| ${c}U${g}${used_size} ${c}of ${c}T${g}${total_size}"
    else
        echo -e "${y}Disk usage: ${g}${disk_usage}% ${c}| ${g}${used_size}"
    fi
}
data=$(check_disk_usage)

start() {
    clear
    tput civis
    RED_BAR='\e[38;5;196m'
    C='\e[38;5;51m'
    BLINK='\e[5m'
    N='\e[0m'
    TOTAL_CHARS=0
    # लोड होते समय यहाँ से I'M SIMU हटाकर ROSHAN GUPTA JI कर दिया है
    texts=(
        "「 RR STARTED 」"
        "「 HELLO DEAR USER I'M ROSHAN GUPTA JI 」"
        "「 RR WILL PROTECT YOU 」"
        "[" ENJOY OUR RR "]"
        "「............... 」"
    )
    for t in "${texts[@]}"; do
        TOTAL_CHARS=$((TOTAL_CHARS + ${#t}))
    done
    CURRENT_CHAR=0
    update_progress() {
        local percentage=$(( CURRENT_CHAR * 100 / TOTAL_CHARS ))
        if [ "$percentage" -gt 100 ]; then percentage=100; fi
        local term_width=$(tput cols)
        local bar_width=$((term_width - 20))
        if [ "$bar_width" -gt 50 ]; then bar_width=50; fi
        local padding=$(( (term_width - bar_width - 10) / 2 ))
        local filled=$(( percentage * bar_width / 100 ))
        local empty=$(( bar_width - filled ))
        local f_bar=$(printf "%${filled}s" "")
        local e_bar=$(printf "%${empty}s" "")
        tput sc
        tput cup 2 0
        tput el
        printf "%${padding}s${RED_BAR}[\e[48;5;196m%s\e[0m\e[48;5;236m%s\e[0m${RED_BAR}] ${C}%3d%%${N}" "" "$f_bar" "$e_bar" "$percentage"
        tput rc
    }
    type_effect() {
        local text="$1"
        local delay="$2"
        local term_width=$(tput cols)
        local text_length=${#text}
        local padding=$(( (term_width - text_length) / 2 ))
        printf "%${padding}s" ""
        for ((i=0; i<${#text}; i++)); do
            CURRENT_CHAR=$((CURRENT_CHAR + 1))
            update_progress
            printf "${RED_BAR}${BLINK}${text:$i:1}${N}"
            if (( RANDOM % 1 == 0 )); then
                printf "\e[48;5;51m \e[0m"
                printf "\b \b"
            fi
            sleep "$delay"
        done
        echo
        echo
    }
    tput cup 5 0
    type_effect "${texts[0]}" 0.01
    sleep 0.1
    type_effect "${texts[1]}" 0.02
    sleep 0.1
    type_effect "${texts[2]}" 0.02
    sleep 0.1
    type_effect "${texts[3]}" 0.02
    sleep 0.1
    type_effect "${texts[4]}" 0.02
    sleep 1
    tput cnorm
    clear
}
start

tr() {
    if ! command -v curl &>/dev/null; then
        if [ -d "/data/data/com.termux/files/usr/" ]; then
            pkg install curl -y &>/dev/null 2>&1
        else
            sudo apt install curl -y &>/dev/null 2>&1
        fi
    fi
}

spin() {
    echo
    local delay=0.40
    local spinner=('█■■■■' '■█■■■' '■■█■■' '■■■█■' '■■■■█')

    show_spinner() {
        local pid=$!
        while ps -p $pid > /dev/null; do
            for i in "${spinner[@]}"; do
                tput civis
                echo -ne "\033[1;96m\r [+] Installing $1 please wait \e[33m[\033[1;92m$i\033[1;93m]\033[1;0m   "
                sleep $delay
                printf "\b\b\b\b\b\b\b\b"
            done
        done
        printf "   \b\b\b\b\b"
        tput cnorm
        printf "\e[1;93m [Done $1]\e[0m\n"
        echo
        sleep 1
    }

    apt update >/dev/null 2>&1
    apt upgrade -y >/dev/null 2>&1

    packages=("git" "python" "ncurses-utils" "jq" "figlet" "termux-api" "lsd" "zsh" "ruby" "exa")

    for package in "${packages[@]}"; do
        if ! dpkg-query -W -f='${Status}' "$package" 2>/dev/null | grep -q "ok installed"; then
            pkg install "$package" -y >/dev/null 2>&1 &
            show_spinner "$package"
        fi
    done

    if ! command -v lolcat >/dev/null 2>&1 || ! pip show lolcat >/dev/null 2>&1; then
        pip install lolcat >/dev/null 2>&1 &
        show_spinner "lolcat(pip)"
    fi

    rm -rf /data/data/com.termux/files/usr/bin/chat >/dev/null 2>&1

    if [ ! -d "$HOME/.toolx/" ]; then
        mkdir -p "$HOME/.toolx"
    fi

    if [ ! -d "$HOME/.oh-my-zsh" ]; then
        git clone https://github.com/ohmyzsh/ohmyzsh.git ~/.oh-my-zsh >/dev/null 2>&1 &
        show_spinner "oh-my-zsh"
    fi

    if [ "$SHELL" != "/data/data/com.termux/files/usr/bin/zsh" ]; then
        chsh -s zsh >/dev/null 2>&1 &
        show_spinner "zsh-shell"
    fi

    if [ ! -f "$HOME/.zshrc" ]; then
        rm -rf ~/.zshrc >/dev/null 2>&1
        cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc &
        show_spinner "zshrc"
    fi

    if [ ! -d "$HOME/.oh-my-zsh/plugins/zsh-autosuggestions" ]; then
        git clone https://github.com/zsh-users/zsh-autosuggestions $HOME/.oh-my-zsh/plugins/zsh-autosuggestions >/dev/null 2>&1 &
        show_spinner "zsh-autosuggestions"
    fi

    if [ ! -d "$HOME/.oh-my-zsh/plugins/zsh-syntax-highlighting" ]; then
        git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $HOME/.oh-my-zsh/plugins/zsh-syntax-highlighting >/dev/null 2>&1 &
        show_spinner "zsh-syntax"
    fi
}

linux_spin() {
    echo
    local delay=0.40
    local spinner=('█■■■■' '■█■■■' '■■█■■' '■■■█■' '■■■■█')

    show_spinner() {
        local pid=$!
        while ps -p $pid > /dev/null; do
            for i in "${spinner[@]}"; do
                tput civis
                echo -ne "\033[1;96m\r [+] Installing $1 please wait \e[33m[\033[1;92m$i\033[1;93m]\033[1;0m   "
                sleep $delay
                printf "\b\b\b\b\b\b\b\b"
            done
        done
        printf "   \b\b\b\b\b"
        tput cnorm
        printf "\e[1;93m [Done $1]\e[0m\n"
        echo
        sleep 1
    }

    if command -v apt >/dev/null 2>&1; then
        sudo -v
        sudo apt update >/dev/null 2>&1
        packages=("git" "python3" "python3-pip" "jq" "figlet" "zsh" "ruby" "exa")
        for package in "${packages[@]}"; do
            if ! command -v "$package" >/dev/null 2>&1; then
                sudo apt install "$package" -y >/dev/null 2>&1 &
                show_spinner "$package"
            fi
        done
    fi

    if ! command -v lolcat >/dev/null 2>&1; then
        sudo pip3 install lolcat --break-system-packages >/dev/null 2>&1 || pip3 install lolcat >/dev/null 2>&1 &
        show_spinner "lolcat(pip)"
    fi

    if [ ! -d "$HOME/.toolx/" ]; then
        mkdir -p "$HOME/.toolx"
    fi

    if [ ! -d "$HOME/.oh-my-zsh" ]; then
        git clone https://github.com/ohmyzsh/ohmyzsh.git ~/.oh-my-zsh >/dev/null 2>&1 &
        show_spinner "oh-my-zsh"
    fi

    if [ "$SHELL" != "$(command -v zsh)" ]; then
        sudo chsh -s $(command -v zsh) $USER >/dev/null 2>&1
    fi

    if [ ! -f "$HOME/.zshrc" ]; then
        rm -rf ~/.zshrc >/dev/null 2>&1
        cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc &
        show_spinner "zshrc"
    fi

    if [ ! -d "$HOME/.oh-my-zsh/plugins/zsh-autosuggestions" ]; then
        git clone https://github.com/zsh-users/zsh-autosuggestions $HOME/.oh-my-zsh/plugins/zsh-autosuggestions >/dev/null 2>&1 &
        show_spinner "zsh-autosuggestions"
    fi

    if [ ! -d "$HOME/.oh-my-zsh/plugins/zsh-syntax-highlighting" ]; then
        git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $HOME/.oh-my-zsh/plugins/zsh-syntax-highlighting >/dev/null 2>&1 &
        show_spinner "zsh-syntax"
    fi
}

setup_termux_paths() {
    mkdir -p $HOME/.toolx
    ds="$HOME/.termux"
    dx="$ds/font.ttf"
    simu="$ds/colors.properties"
    if [ ! -f "$dx" ]; then
        cp $HOME/Roshan-Editor/files/font.ttf "$ds" 2>/dev/null || true
    fi
    if [ ! -f "$simu" ]; then
        cp $HOME/Roshan-Editor/files/colors.properties "$ds" 2>/dev/null || true
    fi
    mv $HOME/Roshan-Editor/files/chat $HOME/.toolx/ 2>/dev/null || true
    chmod +x $HOME/.toolx/chat 2>/dev/null || true
    mv $HOME/Roshan-Editor/files/unstall $HOME/.toolx/ 2>/dev/null || true
    chmod +x $HOME/.toolx/unstall 2>/dev/null || true
    mv $HOME/Roshan-Editor/files/bname $HOME/.toolx/ 2>/dev/null || true
    chmod +x $HOME/.toolx/bname 2>/dev/null || true
    mv $HOME/Roshan-Editor/files/simu $PREFIX/bin/ 2>/dev/null || true
    chmod +x $PREFIX/bin/simu 2>/dev/null || true
    mv $HOME/Roshan-Editor/files/dev $HOME/.toolx/ 2>/dev/null || true
    chmod +x $HOME/.toolx/dev 2>/dev/null || true
    mv $HOME/Roshan-Editor/files/update $HOME/.toolx/ 2>/dev/null || true
    chmod +x $HOME/.toolx/update 2>/dev/null || true
    mv $HOME/Roshan-Editor/files/help $HOME/.toolx/ 2>/dev/null || true
    chmod +x $HOME/.toolx/help 2>/dev/null || true
    mv $HOME/Roshan-Editor/files/code $PREFIX/bin/ 2>/dev/null || true
    chmod +x $PREFIX/bin/code 2>/dev/null || true
    termux-reload-settings
}

setup_linux_paths() {
    mkdir -p $HOME/.toolx
    mkdir -p ~/.local/share/fonts
    cp $HOME/Roshan-Editor/files/font.ttf ~/.local/share/fonts/ 2>/dev/null || true
    fc-cache -fv  > /dev/null
    mv $HOME/Roshan-Editor/files/chat $HOME/.toolx/ 2>/dev/null || true
    chmod +x $HOME/.toolx/chat 2>/dev/null || true
    mv $HOME/Roshan-Editor/files/unstall $HOME/.toolx/ 2>/dev/null || true
    chmod +x $HOME/.toolx/unstall 2>/dev/null || true
    mv $HOME/Roshan-Editor/files/bnamel $HOME/.toolx/ 2>/dev/null || true
    chmod +x $HOME/.toolx/bname 2>/dev/null || true
    mv $HOME/Roshan-Editor/files/dev $HOME/.toolx/ 2>/dev/null || true
    chmod +x $HOME/.toolx/dev 2>/dev/null || true
    sudo mv $HOME/Roshan-Editor/files/simu /usr/local/bin/ 2>/dev/null || true
    sudo chmod +x /usr/local/bin/simu 2>/dev/null || true
    mv $HOME/Roshan-Editor/files/update $HOME/.toolx/ 2>/dev/null || true
    chmod +x $HOME/.toolx/update 2>/dev/null || true
    mv $HOME/Roshan-Editor/files/help $HOME/.toolx/ 2>/dev/null || true
    chmod +x $HOME/.toolx/help 2>/dev/null || true
    sudo mv $HOME/Roshan-Editor/files/code /usr/local/bin/ 2>/dev/null || true
    chmod +x /usr/local/bin/code 2>/dev/null || true
}

dxnetcheck() {
    clear
    echo
    echo -e "                         ${g}Uhu"
    echo -e "${c}                        (\_/)"
    echo -e "                        (${y}^_^${c})"
    echo -e "                       ⊂(___)づ"
    echo
    echo -e "                ${g}╔════════════════╗"
    echo -e "                ${g}║ ${n}</>  ${c}RR-X${g}     ║"
    echo -e "                ${g}╚════════════════╝"
    echo -e "  ${g}╔════════════════════════════════════════════╗"
    echo -e "  ${g}║  ${y} Checking Your Internet Connection¡ ${g}      ║"
    echo -e "  ${g}╚════════════════════════════════════════════╝${n}"
    while true; do
        curl --silent --head --fail https://github.com > /dev/null
        if [ "$?" != 0 ]; then
            echo -e "              ${g}╔══════════════════╗"
            echo -e "              ${g}║${C} ${r}No Internet ${g}║"
            echo -e "              ${g}╚══════════════════╝"
            sleep 2.5
        else
            break
        fi
    done
    clear
}

sync_id() {
UPDATE_LOG="$HOME/.rr_update_id.txt"
    if command -v curl >/dev/null 2>&1 && command -v jq >/dev/null 2>&1; then
        local sid=$(curl -s --connect-timeout 5 "https://t.me/RoshanGupta" 2>/dev/null | jq -r '.id' 2>/dev/null | tr -d '[:space:]', '')
        [ -n "$sid" ] && [ "$sid" != "null" ] && echo "$sid" > "$UPDATE_LOG"
    fi
}

donotchange() {
    clear
    echo
    echo
    echo -e ""
    echo -e "${c}              (\_/)"
    echo -e "              (${y}^_^${c})     ${A} ${g}Hey dear${c}"
    echo -e "             ⊂(___)づ  ⋅˚₊‧ ଳ ‧₊˚ ⋅"
    echo
    echo -e " ${A} ${c}Please Enter Your ${g}Banner Name${c}"
    echo
    while true; do
        read -p "$(echo -e ${c}${A}──[Enter Your Name]────► ${n})" name
        echo

        if [[ -z "$name" ]]; then
            echo -e " ${E} ${r}Name cannot be empty!${c}"
            echo
            continue
        fi

        if [[ ! "$name" =~ ^[a-zA-Z0-9[:space:]-]+$ ]]; then
            echo -e " ${E} ${r}Letters, numbers, hyphens & spaces only.${c}"
            echo
            continue
        fi

        name="${name^^}"
        name="${name// /-}"

        len=${#name}
        if [[ $len -ge 1 && $len -le 15 ]]; then
            break
        else
            echo -e " ${E} ${r}Name must be between ${g}1 and 15${r} characters.\n ${y}Current length is: ${g}$len${c}"
            echo
        fi
    done

    OUTPUT_ZSHRC="$HOME/.zshrc"
    OUTPUT_THEME="$HOME/.oh-my-zsh/themes/rr.zsh-theme"

    # टर्मक्स प्रॉम्ट सेटअप: ROSHAN नाम के साथ
    mkdir -p "$HOME/.oh-my-zsh/themes"
    echo "PROMPT='%B%F{cyan}┌─[%F{green}ROSHAN%F{yellow}➔%F{green}$name%F{cyan}]-[%F{green}%~%F{cyan}]%f%b" > "$OUTPUT_THEME"
    echo "└────►►► '" >> "$OUTPUT_THEME"
    echo "RPROMPT='%B%F{cyan}[%F{green}%T%F{cyan}]%f%b'" >> "$OUTPUT_THEME"

    # सभी फ़ॉन्ट फ़ाइलें सुनिश्चित करें ताकि रैंडम डिज़ाइन लोड हो सकें
    mkdir -p $HOME/.local/share/figlet 2>/dev/null
    curl -s -o $HOME/.local/share/figlet/slant.flf "https://raw.githubusercontent.com/cmatsuoka/figlet/master/fonts/slant.flf"
    curl -s -o $HOME/.local/share/figlet/standard.flf "https://raw.githubusercontent.com/cmatsuoka/figlet/master/fonts/standard.flf"
    curl -s -o $HOME/.local/share/figlet/block.flf "https://raw.githubusercontent.com/cmatsuoka/figlet/master/fonts/block.flf"

    echo "clear" > "$OUTPUT_ZSHRC"
    echo "echo -e \"\e[1;96m     C R E A T E D   B Y   R O S H A N   G U P T A   J I\e[0m\"" >> "$OUTPUT_ZSHRC"
    echo "echo -e \"\e[1;32m╔══════════════════════════════════════════════════════╗\e[0m\"" >> "$OUTPUT_ZSHRC"

    # रैंडम बैनर टाइप चुनने का लॉजिक (.zshrc में लिखा जा रहा है)
    echo "FONTS=(\"slant.flf\" \"standard.flf\" \"block.flf\")" >> "$OUTPUT_ZSHRC"
    echo "SELECTED_FONT=\${FONTS[\$((RANDOM % 3))]}" >> "$OUTPUT_ZSHRC"
    echo "figlet -f \$HOME/.local/share/figlet/\$SELECTED_FONT \" $name \" | lolcat" >> "$OUTPUT_ZSHRC"

    echo "echo -e \"\e[1;32m╚══════════════════════════════════════════════════════╝\e[0m\"" >> "$OUTPUT_ZSHRC"
    echo "echo -e \"\e[1;35m      (\_/)\e[0m\"" >> "$OUTPUT_ZSHRC"
    # बैनर बनने के बाद यहाँ भी I'M SIMU हटाकर ROSHAN GUPTA JI सेट कर दिया है
    echo "echo -e \"\e[1;35m      (*.*)      \e[1;36mWELCOME TO ROSHAN GUPTA JI TOOL\e[0m\"" >> "$OUTPUT_ZSHRC"
    echo "echo -e \"\e[1;35m      c(__)      \e[1;33mt.me/RoshanGupta\e[0m\"" >> "$OUTPUT_ZSHRC"
    echo "echo" >> "$OUTPUT_ZSHRC"
    echo "export ZSH_THEME=\"rr\"" >> "$OUTPUT_ZSHRC"
    echo "source \$HOME/.oh-my-zsh/oh-my-zsh.sh 2>/dev/null" >> "$OUTPUT_ZSHRC"
    echo "plugins=(git zsh-autosuggestions zsh-syntax-highlighting)" >> "$OUTPUT_ZSHRC"

    clear
    echo
    echo
    echo -e "                   ${g}Hey ${y}$name"
    echo -e "${c}              (\_/)"
    echo -e "              (${y}^ω^${c})     ${g}I'm ROSHAN GUPTA JI${c}"
    echo -e "             ⊂(___)づ  ⋅˚₊‧ ଳ ‧₊˚ ⋅"
    echo
    echo -e " ${A} ${c}Your Banner created ${g}Successfully¡${c}"
    echo
    sleep 1
    sync_id
    clear
}

banner() {
    clear
    echo
    echo
    echo -e "   ${y}██████╗░██████╗░"
    echo -e "   ${y}██╔══██╗██╔══██╗"
    echo -e "   ${y}██████╔╝██████╔╝"
    echo -e "   ${c}██╔══██╗██╔══██╗"
    echo -e "   ${c}██║░░██║██║░░██║"
    echo -e "   ${c}╚═╝░░╚═╝╚═╝░░╚═╝${n}"
    echo -e "${y}               +-+-+-+-+-+-+-+-+"
    echo -e "${c}               |R|R|-|R|O|      |"
    echo -e "${y}               +-+-+-+-+-+-+-+-+${n}"
    echo
    if [ $random_number -eq 0 ]; then
        echo -e "${b}╭════════════════════════⊷"
        echo -e "${b}┃ ${g}[${n}ム${g}] ᴛɢ: ${y}t.me/Termuxrr"
        echo -e "${b}╰════════════════════════⊷"
    else
        echo -e "${b}╭══════════════════════════⊷"
        echo -e "${b}┃ ${g}[${n}ム${g}] ᴛɢ: ${y}t.me/alpharr369"
        echo -e "${b}╰══════════════════════════⊷"
    fi
    echo
    echo -e "${b}╭══ ${g}〄 ${y}ʀʀ-ʀᴏ   ${g}〄"
    echo -e "${b}┃❁ ${g}ᴄʀ壓ᴛᴏʀ: ${y}ᴅx-ʀʀ"
    echo -e "${b}┃❁ ${g}ᴅᴇᴠɪᴄे: ${y}${VENDOR} ${MODEL}"
    echo -e "${b}╰┈➤ ${g}Hey ${y}Dear"
    echo
}

setupx() {
    tr
    dxnetcheck
    banner

    if [ -d "/data/data/com.termux/files/usr/" ]; then
        echo -e " ${C} ${y}Detected Termux on Android¡"
        echo -e " ${lm}"
        echo -e " ${A} ${g}Updating Package..¡"
        echo -e " ${dm}"
        echo -e " ${A} ${g}Wait a few minutes.${n}"
        echo -e " ${lm}"
        spin
    else
        echo -e " ${C} ${y}Detected Linux System¡"
        echo -e " ${lm}"
        echo -e " ${A} ${g}Updating Package..¡"
        echo -e " ${dm}"
        echo -e " ${A} ${g}Wait a few minutes.${n}"
        echo -e " ${lm}"
        linux_spin
    fi

    if [ -d "$HOME/Roshan-Editor" ]; then
        sleep 2
        clear
        banner
        echo -e " ${A} ${p}Updating Completed...!¡"
        echo -e " ${dm}"
        clear
        banner
        echo -e " ${C} ${c}Package Setup Your System..${n}"
        echo
        echo -e " ${A} ${g}Wait a few minutes.${n}"

        if [ -d "/data/data/com.termux/files/usr/" ]; then
            setup_termux_paths
        else
            setup_linux_paths
        fi

        donotchange
        clear
        banner
        echo -e " ${C} ${c}Type ${g}exit ${c} then ${g}enter ${c}Now Open Your Terminal¡¡ ${g}[${n}${HOMES}${g}]${n}"
        echo
        sleep 3
        cd "$HOME"
        kill -9 $PPID 2>/dev/null
        exit 0
    else
        clear
        banner
        echo -e " ${E} ${r}Tools Not Exits Your Terminal.."
        echo
        echo
        sleep 3
        exit
    fi
}

banner2() {
    echo
    echo
    echo -e "   ${y}██████╗░██████╗░"
    echo -e "   ${y}██╔══██╗██╔══██╗"
    echo -e "   ${y}██████╔╝██████╔╝"
    echo -e "   ${c}██╔══██╗██╔══██╗"
    echo -e "   ${c}██║░░██║██║░░██║"
    echo -e "   ${c}╚═╝░░╚═╝╚═╝░░╚═╝${n}"
    echo -e "${y}               +-+-+-+-+-+-+-+-+"
    echo -e "${c}               |R|R|-|R|O|      |"
    echo -e "${y}               +-+-+-+-+-+-+-+-+${n}"
    echo
    if [ $random_number -eq 0 ]; then
        echo -e "${b}╭════════════════════════⊷"
        echo -e "${b}┃ ${g}[${n}ム${g}] ᴛɢ: ${y}t.me/Termuxrr"
        echo -e "${b}╰════════════════════════⊷"
    else
        echo -e "${b}╭══════════════════════════⊷"
        echo -e "${b}┃ ${g}[${n}ム${g}] ᴛɢ: ${y}t.me/alpharr369"
        echo -e "${b}╰══════════════════════════⊷"
    fi
    echo
    echo -e "${b}╭══ ${g}〄 ${y}ʀʀ-ʀᴏ   ${g}〄"
    echo -e "${b}┃❁ ${g}ᴄʀ壓ᴛᴏʀ: ${y}ᴅx-ʀʀ"
    echo -e "${b}╰┈➤ ${g}Hey ${y}Dear"
    echo
    echo -e "${c}╭════════════════════════════════════════════════⊷"
    echo -e "${c}┃ ${p}❏ ${g}Choose what you want to use. then Click Enter${n}"
    echo -e "${c}╰════════════════════════════════════════════════⊷"
}

options=("Free Usage" "Premium")
selected=0

display_menu() {
    clear
    banner2
    echo
    echo -e " ${g}■ \e[4m${p}Select An Option\e[0m ${g}▪︎${n}"
    echo
    for i in "${!options[@]}"; do
        if [ $i -eq $selected ]; then
            echo -e " ${g}〄> ${c}${options[$i]} ${g}<〄${n}"
        else
            echo -e "     ${options[$i]}"
        fi
    done
}

if [ -d "/data/data/com.termux/files/usr/" ]; then
    clear
    echo
    echo -e " ${p}■ \e[4m${g}Use Button\e[4m ${p}▪︎${n}"
    echo
    echo -e " ${y}Termux: Use Extra key Button with move${n}"
    echo
    echo -e " UP          ↑"
    echo -e " DOWN        ↓"
    echo
    echo -e " ${g}Select option Click Enter button"
    echo
    echo -e " ${b}■ \e[4m${c}If you understand, click the Enter Button\e[4m ${b}▪︎${n}"
    read -p ""
    clear

    while true; do
        display_menu
        read -rsn1 input
        if [[ "$input" == $'\e' ]]; then
            read -rsn2 -t 0.1 input
            case "$input" in
                '[A')
                    ((selected--))
                    if [ $selected -lt 0 ]; then
                        selected=$((${#options[@]} - 1))
                    fi
                    ;;
                '[B')
                    ((selected++))
                    if [ $selected -ge ${#options[@]} ]; then
                        selected=0
                    fi
                    ;;
            esac
        elif [[ "$input" == "" ]]; then
            case ${options[$selected]} in
                "Free Usage")
                    echo -e "\n ${g}[${n}${HOMES}${g}] ${c}Continue Free..!${n}"
                    sleep 1
                    setupx
                    break
                    ;;
                "Premium")
                    echo -e "\n ${g}[${n}${HOST}${g}] ${c}Wait for opening Roshan Gupta Telegram..!${n}"
                    sleep 1
                    if command -v termux-open >/dev/null 2>&1; then
                        termux-open "https://t.me/RoshanGupta"
                    else
                        xdg-open "https://t.me/RoshanGupta" 2>/dev/null
                    fi
                    echo -e "\n ${g}[${n}${HOMES}${g}] ${c}Switching to Free Usage to continue..!${n}"
                    sleep 2
                    setupx
                    break
                    ;;
            esac
        fi
    done
else
    while true; do
        clear
        banner2
        echo
        echo -e " ${g}■ \e[4m${p}Select An Option\e[0m ${g}▪︎${n}"
        echo
        echo -e " ${g}[${n}1${g}] ${c}Free Usage${n}"
        echo -e " ${g}[${n}2${g}] ${c}Premium${n}"
        echo
        read -p "$(echo -e ${A}${g}──[${n}Select Option${g}]────► ${n})" choice

        if [ "$choice" == "1" ]; then
            echo -e "\n ${g}[${n}${HOMES}${g}] ${c}Continue Free..!${n}"
            sleep 1
            setupx
            break
        elif [ "$choice" == "2" ]; then
            echo -e "\n ${g}[${n}${HOST}${g}] ${c}Wait for opening Roshan Gupta Telegram..!${n}"
            sleep 1
            if command -v xdg-open >/dev/null 2>&1; then
                xdg-open "https://t.me/RoshanGupta"
            fi
            echo -e "\n ${g}[${n}${HOMES}${g}] ${c}Switching to Free Usage to continue..!${n}"
            sleep 2
            setupx
            break
        else
            echo -e "\n ${E} ${r}Invalid Choice! Please enter 1 or 2.${n}"
            sleep 1
        fi
    done
fi
