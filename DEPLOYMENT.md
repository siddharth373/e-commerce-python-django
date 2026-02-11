# Vercel Deployment Guide

## ✅ Completed Setup Steps

1. **Git Initialized & Pushed to GitHub**
   - Repository: https://github.com/siddharth373/e-commerce-python-django.git
   - Branch: main
   - All files committed and pushed

2. **Configuration Files Created**
   - `vercel.json` - Vercel build configuration
   - `requirements.txt` - Updated with production dependencies (gunicorn, whitenoise)
   - `shop_project/settings.py` - Updated for production (WhiteNoise middleware, environment variables)
   - `.env.example` - Environment variable template

## 🚀 Deploy to Vercel (Next Steps)

### Step 1: Connect GitHub Repository to Vercel
1. Go to [vercel.com](https://vercel.com) and sign in with your GitHub account
2. Click **"Add New..."** → **"Project"**
3. Select your repository: `e-commerce-python-django`
4. Click **"Import"**

### Step 2: Configure Environment Variables
In the Vercel project settings, add these environment variables:

```
SECRET_KEY=your-secure-random-key-here
DEBUG=False
ALLOWED_HOSTS=your-project-name.vercel.app,localhost,127.0.0.1
```

**To generate a SECRET_KEY:**
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### Step 3: Configure Build & Output Settings
In Vercel dashboard:
- **Framework Preset:** Other (for Python)
- **Build Command:** `pip install -r requirements.txt`
- **Output Directory:** (leave blank)
- **Install Command:** `pip install -r requirements.txt`

### Step 4: Deploy
1. Click **"Deploy"** button
2. Wait for build to complete (usually 2-5 minutes)
3. Visit your deployed app at `https://your-project-name.vercel.app`

## ⚙️ Important Notes

### Database
- Currently configured with SQLite (`db.sqlite3`)
- SQLite won't persist on Vercel (serverless environment)
- **For production, migrate to PostgreSQL:**
  1. Create free PostgreSQL at [neon.tech](https://neon.tech) or Supabase
  2. Update `settings.py` to use PostgreSQL
  3. Set `DATABASE_URL` environment variable in Vercel

### Static Files
- WhiteNoise middleware is configured to serve static files
- Run `python manage.py collectstatic` locally if you add static files

### First Deployment Debugging
- Check Vercel build logs if deployment fails
- The build should show all dependencies installing correctly
- If you get import errors, verify all required packages are in `requirements.txt`

## 🔧 Running Locally Before Deployment

```bash
# Install dependencies
pip install -r requirements.txt

# Create .env file with your SECRET_KEY
cp .env.example .env

# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

## 📚 Troubleshooting

### Build fails with "ModuleNotFoundError"
- Ensure the package is in `requirements.txt`
- Try deleting `venv/` and reinstalling: `pip install -r requirements.txt`

### Static files not loading
- Verify `STATIC_ROOT` is set correctly
- Run: `python manage.py collectstatic`
- Check Vercel logs for whitenoise errors

### Database migration issues
- For production, use a managed database service
- Update `settings.py` database config and add `DATABASE_URL` env var

### CSRF errors in production
- Ensure `ALLOWED_HOSTS` includes your Vercel domain
- Check that `DEBUG=False` in production

## 📖 Useful Links
- [Vercel Python Support](https://vercel.com/docs/frameworks/python)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)
- [WhiteNoise Documentation](http://whitenoise.evans.io/)
