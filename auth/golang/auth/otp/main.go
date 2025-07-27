package main

import (
	"fmt"
	"os"

	"github.com/mdp/qrterminal/v3"
	"github.com/xlzd/gotp"
)

func main() {
	secret := "4S62BZNFXXSZLCRO"
	accountName := "myCoolAccount"
	issuer := "MyCoolCompany"
	// TOTP := gotp.OtpTypeTotp
	totp := gotp.NewDefaultTOTP(secret)
	url := totp.ProvisioningUri(accountName, issuer)

	// qrterminal.Generate(url, qrterminal.L, os.Stdout)
	config := qrterminal.Config{
		HalfBlocks: true,
		Level:      qrterminal.M,
		Writer:     os.Stdout,
	}
	qrterminal.GenerateWithConfig(url, config)

	// fmt.Println(gotp.BuildUri(TOTP, secret, accountName, issuer,))
	fmt.Println("Current OTP is", gotp.NewDefaultTOTP(secret).Now())
}

