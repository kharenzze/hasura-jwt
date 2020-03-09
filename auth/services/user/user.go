package user

import (
	"fmt"
	"github.com/go-resty/resty/v2"
)

//client

type User struct {
	id string `json:"id"`
	email string `json:"email"`
}

type UserResponse struct {
		User []User `json:"user"`
}

type Query struct {
	Query string `json:"query"`
}


func FetchOneUser() {
	client :=  resty.New()
	client.SetDebug(true)
	queryText := `
		query {
			user(limit: 1) {
				id
				email
			}
		}
	`
	body := Query{Query:queryText}
	resp, err := client.R().
		SetHeader("Content-Type", "application/json").
		SetBody(body).
		//SetResult(&AuthSuccess{}).    // or SetResult(AuthSuccess{}).
		Post("http://0.0.0.0:8080/v1/graphql")
	fmt.Println(err)
	fmt.Println(resp)
}


