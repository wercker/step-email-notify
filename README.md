# email-notify

Send an email message

## Options

### required

* `from` - From address.
* `to` - To address.
* `host` - The host of your SMTP server.
* `username` - The username for your SMTP server.
* `password` - The password for your SMTP server.

### optional

* `passed-subject` - Use this option to override the default passed subject.
* `failed-subject` -  Use this option to override the default failed subject.
* `passed-body` - Use this option to specify the passed body.
* `failed-body` -  Use this option to specify the failed body.
* `on` - Possible values: `always` and `failed`, default `always`


# Example

Add EMAIL_PASSWORD as deploy target or application environment variable.

``` yaml
    build:
        after-steps:
            - email-notify:
                from: alerts@wercker.com
                to: you@company.com
                username: username
                password: $EMAIL_PASSWORD
                host: smtp.gmail.com:587
```

# Changelog
## 1.1.0
- added result (passed/failed) message for build and deploys

## 1.0.1:
- library embedded for sending email messages
- add sensible default message. Just like s-kawaguchi's [email-notify step](https://github.com/s-kawaguchi/wercker-step-email-notify)

## 1.0.0:
- initial release
