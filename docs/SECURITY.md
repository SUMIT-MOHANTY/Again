# Security Documentation

## Placeholder Certificate
The repository includes a self‑signed placeholder certificate located at `./certs/placeholder.crt` and its private key at `./certs/placeholder.key`. These are **not** suitable for production.

## Replacing with Production Certificates
1. Obtain a certificate and key from a trusted CA (e.g., Let's Encrypt) for your domain.
2. Place the certificate file at `./certs/your_cert.crt` and the key at `./certs/your_key.key`.
3. Update the environment variables `CERT_PATH` and `KEY_PATH` (or modify `backend/config.py`) to point to the new files.
4. Re‑build and re‑deploy the Docker containers.

## Renewal Process
- For Let's Encrypt, set up automatic renewal using `certbot renew` and copy the renewed files into the `./certs` directory before each deployment.
- If using an internal PKI, follow your organization's renewal workflow and update the mounted files similarly.

The application will automatically pick up the paths from the environment variables and serve traffic over HTTPS on port **8443**.
