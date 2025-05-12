# Config
$bootPath = "D:\"  # Change this to your SD card's boot drive letter
$wifiSSID = "VZ_104MAVER"
$wifiPassword = "VaKis-!10-mayFNA@23"
$countryCode = "US"

# Enable SSH
$sshFile = Join-Path $bootPath "ssh"
New-Item -ItemType File -Path $sshFile -Force | Out-Null
Write-Host "✅ SSH enabled"

# Create wpa_supplicant.conf with properly escaped quotes
$wifiConf = @"
country=$countryCode
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid=`"$wifiSSID`"
    psk=`"$wifiPassword`"
    key_mgmt=WPA-PSK
}
"@

$wifiFile = Join-Path $bootPath "wpa_supplicant.conf"
Set-Content -Path $wifiFile -Value $wifiConf -Encoding ASCII
Write-Host "✅ Wi-Fi configured for SSID: $wifiSSID"

Write-Host "🎉 Done! Insert the SD card into your Raspberry Pi and power it on."
Write-Host "Try connecting via 'ssh pi@raspberrypi.local'"



