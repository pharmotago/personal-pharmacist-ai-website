# Shopify Integration Guide for Personal Pharmacist AI

This guide explains how to integrate the Personal Pharmacist AI marketing website into your Shopify store.

## 📋 Prerequisites

- Shopify store with theme editing access
- Basic understanding of Shopify Liquid templating
- FTP/file upload capabilities

## 🔧 Integration Methods

### Method 1: Custom Page Template (Recommended)

1. **Create Custom Page Template**
   - Navigate to Online Store > Themes > Actions > Edit code
   - In Templates folder, create `page.personal-pharmacist.liquid`
   - Copy the HTML content from `index.html` into this template
   - Wrap content in Shopify page structure:

```liquid
{% comment %} Personal Pharmacist AI Landing Page {% endcomment %}
<div class="personal-pharmacist-landing">
  <!-- Copy HTML content from index.html here -->
</div>
```

2. **Upload Assets**
   - Upload `assets/index-*.css` to Assets folder
   - Upload `assets/index-*.js` to Assets folder
   - Reference in template:

```liquid
{{ 'index-CuHyLpdr.css' | asset_url | stylesheet_tag }}
{{ 'index-DG6bMjfX.js' | asset_url | script_tag }}
```

3. **Create Landing Page**
   - Navigate to Online Store > Pages
   - Create new page titled "Personal Pharmacist AI"
   - Set template to `page.personal-pharmacist`
   - URL will be: `yourstore.com/pages/personal-pharmacist-ai`

### Method 2: Custom Section

1. **Create Section File**
   - In Sections folder, create `personal-pharmacist-hero.liquid`
   - Convert HTML sections to Liquid sections with schema

2. **Add to Homepage**
   - Use theme customizer to add section to homepage
   - Position prominently for maximum visibility

### Method 3: Complete Landing Page

1. **Replace Homepage Template**
   - Backup current `index.liquid`
   - Replace with Personal Pharmacist AI content
   - Ideal for dedicated health stores

## 🎨 Shopify-Specific Customizations

### Liquid Variables Integration

```liquid
{% comment %} Dynamic store information {% endcomment %}
<h1>{{ shop.name }} presents Personal Pharmacist AI</h1>
<p>Trusted by {{ shop.name }} customers</p>
```

### Product Integration

```liquid
{% comment %} Link to related health products {% endcomment %}
{% assign health_products = collections.health.products %}
<div class="related-products">
  {% for product in health_products limit: 3 %}
    <a href="{{ product.url }}">{{ product.title }}</a>
  {% endfor %}
</div>
```

### Customer Account Integration

```liquid
{% if customer %}
  <p>Welcome back, {{ customer.first_name }}!</p>
  <p>Continue your health journey with Personal Pharmacist AI</p>
{% else %}
  <p>Join thousands of {{ shop.name }} customers using Personal Pharmacist AI</p>
{% endif %}
```

## 📱 Mobile Optimization

Ensure mobile responsiveness in Shopify:

```liquid
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

## 🔗 Navigation Integration

### Add to Main Menu

1. Navigate to Online Store > Navigation
2. Add menu item:
   - **Link**: `/pages/personal-pharmacist-ai`
   - **Label**: "Personal Pharmacist AI"
   - **Position**: Primary navigation

### Breadcrumb Integration

```liquid
<nav class="breadcrumb">
  <a href="/">{{ shop.name }}</a>
  <span>/</span>
  <span>Personal Pharmacist AI</span>
</nav>
```

## 🎯 SEO Optimization

### Page Settings

```liquid
{% comment %} SEO meta tags {% endcomment %}
<title>Personal Pharmacist AI - {{ shop.name }}</title>
<meta name="description" content="AI-powered medication guidance and health recommendations. Trusted by {{ shop.name }} for reliable health information.">
```

### Schema Markup

```liquid
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Personal Pharmacist AI",
  "description": "AI-powered medication guidance platform",
  "provider": {
    "@type": "Organization",
    "name": "{{ shop.name }}",
    "url": "{{ shop.url }}"
  }
}
</script>
```

## 📊 Analytics Integration

### Shopify Analytics

```liquid
{% comment %} Track page views {% endcomment %}
<script>
  gtag('event', 'page_view', {
    'page_title': 'Personal Pharmacist AI Landing',
    'page_location': window.location.href
  });
</script>
```

### Conversion Tracking

```liquid
{% comment %} Track CTA clicks {% endcomment %}
<script>
  document.querySelectorAll('[href*="personalpharmacistAI.replit.app"]').forEach(link => {
    link.addEventListener('click', () => {
      gtag('event', 'click', {
        'event_category': 'CTA',
        'event_label': 'Personal Pharmacist AI Launch'
      });
    });
  });
</script>
```

## 🛒 E-commerce Integration

### Related Products Section

```liquid
{% assign supplements = collections.supplements.products %}
<section class="related-products">
  <h3>Recommended Health Products</h3>
  <div class="product-grid">
    {% for product in supplements limit: 4 %}
      <div class="product-card">
        <img src="{{ product.featured_image | img_url: '300x300' }}" alt="{{ product.title }}">
        <h4>{{ product.title }}</h4>
        <p>{{ product.price | money }}</p>
        <a href="{{ product.url }}" class="btn">View Product</a>
      </div>
    {% endfor %}
  </div>
</section>
```

### Cross-selling Opportunities

```liquid
{% comment %} Promote health consultations {% endcomment %}
<div class="consultation-upsell">
  <h3>Need Personal Guidance?</h3>
  <p>Book a consultation with our health experts</p>
  <a href="/pages/consultation-booking" class="btn btn-secondary">Book Consultation</a>
</div>
```

## 🔒 Legal Compliance

### Terms Integration

```liquid
<p class="legal-notice">
  By using Personal Pharmacist AI, you agree to our 
  <a href="{{ pages.terms-of-service.url }}">Terms of Service</a> and 
  <a href="{{ pages.privacy-policy.url }}">Privacy Policy</a>.
</p>
```

### Medical Disclaimer

```liquid
<div class="medical-disclaimer">
  <h4>Important Medical Disclaimer</h4>
  <p>Personal Pharmacist AI provides educational information only. Always consult with healthcare professionals before making medical decisions. {{ shop.name }} and Personal Pharmacist AI assume no medical liability.</p>
</div>
```

## 🚀 Performance Optimization

### Asset Loading

```liquid
{% comment %} Preload critical assets {% endcomment %}
<link rel="preload" href="{{ 'index-CuHyLpdr.css' | asset_url }}" as="style">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```

### Image Optimization

```liquid
{% comment %} Use Shopify's image transformation {% endcomment %}
<img src="{{ 'hero-image.jpg' | asset_url | img_url: '1200x600' }}" 
     srcset="{{ 'hero-image.jpg' | asset_url | img_url: '600x300' }} 600w,
             {{ 'hero-image.jpg' | asset_url | img_url: '1200x600' }} 1200w"
     alt="Personal Pharmacist AI">
```

## 🧪 Testing Checklist

- [ ] Page loads correctly on desktop and mobile
- [ ] All CTAs link to `https://personalpharmacistAI.replit.app`
- [ ] Shopify navigation integration works
- [ ] Analytics tracking functions properly
- [ ] Legal disclaimers are prominently displayed
- [ ] Page speed scores above 90 on PageSpeed Insights
- [ ] Cross-browser compatibility verified

## 📞 Support

For integration assistance or custom development, contact your Shopify developer or the Personal Pharmacist AI team.

---

Ready to boost your health store's digital presence with AI-powered solutions