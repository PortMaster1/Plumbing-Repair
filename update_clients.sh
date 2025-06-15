cat <<EOF | sudo tee -a /etc/freeradius/3.0/clients.conf > /dev/null

client $3 {
    ipaddr = $1
    secret = $2
    shortname = $3
}
EOF