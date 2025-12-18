# EXERCISE 2

### My answer for the customer would be the following:

Hi <customer name>, thank you for reaching out! Port supports several SSO integrations using standards such as SAML (Microsoft Entra ID, Okta, JumpCloud, Google Workspace), OIDC (Microsoft Entra ID, Okta, OneLogin), and LDAP. Since you’re using Okta, you can integrate with Port using either SAML or OIDC, depending on your preference.

For SAML, please create an App Integration in your Okta account and select the SAML sign-in method. In the SAML settings, configure the Single Sign-On URL as https://auth.getport.io/login/callback?connection={customer_name123} and the Audience URI as urn:auth0:port-prod:{customer_name123}. Next, generate a certificate in PEM format from the Sign On tab under SAML Signing Certificates, and share it with us along with your Identity Provider metadata URL, which can also be found in the Sign On tab. You can follow this step-by-step guide for additional help: [Okta (SAML) | Port](https://docs.port.io/sso-rbac/sso-providers/saml/okta/).

If you prefer OIDC, create an App Integration, choose OIDC with a Single Page Application, enable all grant types, and set the Sign-in redirect URI to https://auth.us.getport.io/login/callback. Under Assignments, allow everyone in your organization to access the app. In General Settings, set Login initiated by to “Either Okta or App,” ensure the login flow is “Redirect to app,” and set the Initiate login URI to https://auth.us.getport.io/authorize?response_type=token&client_id=4lHUry3Gkds317lQ3JcgABh0JPbT3rWx&connection={customer_name123}&redirect_uri=https%3A%2F%2Fapp.us.getport.io. Once configured, please share with us your Okta Domain (in the format {YOUR_COMPANY_NAME}.okta.com) and the Client ID from the app’s General tab. A detailed guide is available here: [Okta (OIDC) | Port](https://docs.port.io/sso-rbac/sso-providers/oidc/okta/).
</div>
