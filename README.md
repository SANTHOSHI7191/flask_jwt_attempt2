# JWT Deploy

A Flask-based JWT authentication API ready for Vercel deployment.

## Features

- JWT-based authentication
- Login endpoint with username/password validation
- Protected routes requiring valid JWT tokens
- Health check endpoint

## Endpoints

- `GET /health` - Health check
- `POST /login` - Login and get JWT access token (requires `username` and `password` headers)
- `POST /protected` - Protected endpoint (requires valid JWT token)

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python api/index.py
```

## Deployment to Vercel

1. Push your code to GitHub
2. Go to [vercel.com](https://vercel.com)
3. Import your repository
4. Add environment variable: `JWT_SECRET_KEY` (set a strong secret key)
5. Deploy

### Environment Variables

Create a `.env.local` file for local development or set these in Vercel:

- `JWT_SECRET_KEY` - Secret key for JWT signing (required for production)

## Testing

### Login
```bash
curl -X POST http://localhost:5000/login \
  -H "username: santhoshi@gmail.com" \
  -H "password: 1234567890"
```

### Access Protected Route
```bash
curl -X POST http://localhost:5000/protected \
  -H "Authorization: Bearer <access_token>"
```

### Health Check
```bash
curl http://localhost:5000/health
```
