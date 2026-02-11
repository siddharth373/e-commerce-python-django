# Quick Start Guide

## ✅ Project Status: COMPLETE

Your Django e-commerce application with AI-powered product recommendations is fully set up and running!

## 🚀 Starting the Application

The server is already running at: **http://127.0.0.1:8000/**

### To Restart the Server (if needed)
```bash
cd c:\Users\SID\Downloads\assignment
.venv\Scripts\activate
python manage.py runserver
```

## 📱 Using the Application

### Step 1: Browse Products
- Visit http://127.0.0.1:8000/
- See all 5 sample products in a beautiful grid layout
- Click on any product to view details

### Step 2: Explore Product Details
- Click a product (e.g., "Blue Jeans")
- View full description and price
- See "Similar Products" recommendations at the bottom
- Add item to cart with the button

### Step 3: Give Feedback
- On product detail page, find the "How do you feel?" section
- Click 👍 **Like** to indicate you like this product
- Click 👎 **Dislike** if you don't want similar items
- Your feedback improves personalized recommendations

### Step 4: Visit AI Recommendations
- Click "AI Recommendations" in the top navigation
- See products picked just for you based on your likes
- The system learns from your preferences in real-time

### Step 5: Shop
- Add products to cart from any page
- Click "Cart" to view your items
- See product names, quantities, and subtotals
- Click "Proceed to Checkout" to complete your order

## 📊 Key Features

### 1. E-Commerce Platform ✅
- Product browsing with grid layout
- Shopping cart with session persistence
- Checkout process with confirmation
- Cart totals and item management

### 2. AI Recommendation System ✅
- Uses product descriptions for similarity analysis
- TF-IDF (Term Frequency-Inverse Document Frequency) algorithm
- Learns from your like/dislike feedback
- Real-time personalization

### 3. Cython Optimization ✅
- Fast similarity calculations for recommendations
- Graceful fallback to pure Python if not compiled
- Application works perfectly either way

### 4. Beautiful UI ✅
- Modern gradient styling with purple and blue colors
- Responsive card-based design
- Smooth animations and hover effects
- Clear navigation and user feedback

## 💾 Sample Data

Pre-loaded products:
1. 🔴 **Red T-Shirt** - Comfortable red t-shirt ($19.99)
2. 👖 **Blue Jeans** - Stylish blue jeans ($49.99)
3. 👟 **Sneakers** - Running sneakers ($79.99)
4. ☕ **Coffee Mug** - Ceramic mug for coffee ($9.99)
5. 🖱️ **Wireless Mouse** - Ergonomic wireless mouse ($24.99)

To reset data: `python manage.py seed`

## 🔧 Tech Stack

- **Back-end**: Django 6.0.2 (Python)
- **ML Algorithm**: TF-IDF Vectorization + Cosine Similarity
- **Optimization**: Cython (C-compiled Python)
- **Database**: SQLite3
- **Frontend**: HTML5 + Responsive CSS

## 📁 Project Structure

```
c:\Users\SID\Downloads\assignment\
├── manage.py                    # Django management
├── db.sqlite3                   # Database (auto-created)
├── requirements.txt             # Python dependencies
├── setup.py                     # Cython build config
├── README.md                    # Full documentation
├── IMPLEMENTATION_NOTES.md      # Technical details
├── shop_project/                # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── store/                       # Main app
    ├── models.py               # Product model
    ├── views.py                # View handlers
    ├── urls.py                 # URL routing
    ├── recommender.py          # ML recommendation engine
    ├── apps.py
    ├── cython_utils/           # Optimized similarity
    │   ├── fast_similarity.pyx
    │   └── fast_similarity.c
    ├── management/
    │   └── commands/
    │       └── seed.py         # Database seeding
    ├── migrations/
    │   └── 0001_initial.py
    └── templates/store/        # HTML templates
        ├── base.html
        ├── product_list.html
        ├── product_detail.html
        ├── cart.html
        ├── checkout.html
        └── recommendations.html
```

## 🎯 Testing Recommendations

Try this workflow to see the AI system in action:

1. **Visit** http://127.0.0.1:8000/
2. **Click** on "Blue Jeans" product
3. **Like** the Blue Jeans (👍 button)
4. **Go back** to home, click "Sneakers"
5. **Check** the recommendations - they're different!
6. **Click** on "AI Recommendations" in nav
7. **Notice** products are ranked by relevance to your likes

The system learns instantly - no training time needed!

## ❓ Troubleshooting

### Server won't start?
```bash
# Make sure you're in the right directory
cd c:\Users\SID\Downloads\assignment

# Activate virtual environment
.venv\Scripts\activate

# Try again
python manage.py runserver
```

### Port 8000 already in use?
```bash
# Use a different port
python manage.py runserver 8080
```

### Need to reset everything?
```bash
# Delete database
del db.sqlite3

# Recreate it
python manage.py migrate
python manage.py seed
```

## 📚 Documentation

- **README.md** - Full feature documentation and setup guide
- **IMPLEMENTATION_NOTES.md** - Technical deep-dive into the recommendation algorithm, Cython optimization, and architecture

## 🎓 Learning Outcomes

You now have a complete example of:
- ✅ Professional Django web development
- ✅ Machine learning integration (TF-IDF + recommendations)
- ✅ Performance optimization with Cython
- ✅ User-facing AI features
- ✅ Beautiful, responsive web design
- ✅ Session management and state persistence

## 🚀 Next Steps

Try enhancing the project:
- Add user authentication for persistent recommendations
- Integrate real payment processing (Stripe, PayPal)
- Add product images and more details
- Implement collaborative filtering (user-to-user recommendations)
- Add search functionality
- Create admin dashboard for product management
- Deploy to web server (Heroku, AWS, etc.)

---

**Status**: ✅ READY TO USE  
**Server**: http://127.0.0.1:8000/  
**Database**: SQLite3 (db.sqlite3)  
**Python**: 3.14.3 Virtual Environment  
**Last Updated**: February 11, 2026

Enjoy your e-commerce app! 🛒
