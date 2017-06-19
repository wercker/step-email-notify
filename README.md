# email-notify

Send an email message (note: requires python 2.x)

[![wercker status](https://app.wercker.com/status/f1ad210ce6c88ed8b437f1e08cc1e213/m "wercker status")](https://app.wercker.com/project/bykey/f1ad210ce6c88ed8b437f1e08cc1e213)

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
* `branch` - Use this option to specify the branch for which an email should be sent.
             If not specified, the email will be sent for builds of all branches.


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
                branch: master
```

# Changelog
## 1.2.0
- added option to specify branch

## 1.1.0
- added result (passed/failed) message for build and deploys

## 1.0.1:
- library embedded for sending email messages
- add sensible default message. Just like s-kawaguchi's [email-notify step](https://github.com/s-kawaguchi/wercker-step-email-notify)

## 1.0.0:
- initial release
