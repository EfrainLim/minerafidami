<!-- Mobile menu JavaScript -->
<script>
    document.addEventListener('DOMContentLoaded', function() {
        const mobileMenuButton = document.getElementById('mobile-menu-button');
        const mobileMenu = document.getElementById('mobile-menu');
        
        if (mobileMenuButton && mobileMenu) {
            // Toggle main mobile menu
            mobileMenuButton.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                mobileMenu.classList.toggle('hidden');
                console.log('Mobile menu toggled:', !mobileMenu.classList.contains('hidden'));
            });
            
            // Handle mobile dropdowns
            const mobileDropdownToggles = mobileMenu.querySelectorAll('.mobile-dropdown-toggle');
            mobileDropdownToggles.forEach(toggle => {
                toggle.addEventListener('click', function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    
                    const dropdown = this.closest('.mobile-dropdown');
                    const content = dropdown.querySelector('.mobile-dropdown-content');
                    const icon = this.querySelector('svg');
                    
                    // Toggle dropdown content
                    content.classList.toggle('hidden');
                    
                    // Rotate icon
                    if (content.classList.contains('hidden')) {
                        icon.classList.remove('rotate-180');
                    } else {
                        icon.classList.add('rotate-180');
                    }
                    
                    console.log('Mobile dropdown toggled:', !content.classList.contains('hidden'));
                });
            });
            
            // Close mobile menu when clicking on a link
            const mobileMenuLinks = mobileMenu.querySelectorAll('a');
            mobileMenuLinks.forEach(link => {
                link.addEventListener('click', function() {
                    mobileMenu.classList.add('hidden');
                    // Reset all dropdowns
                    const allDropdowns = mobileMenu.querySelectorAll('.mobile-dropdown-content');
                    const allIcons = mobileMenu.querySelectorAll('.mobile-dropdown-toggle svg');
                    allDropdowns.forEach(dropdown => dropdown.classList.add('hidden'));
                    allIcons.forEach(icon => icon.classList.remove('rotate-180'));
                    console.log('Mobile menu closed by link click');
                });
            });
            
            // Close mobile menu when clicking outside
            document.addEventListener('click', function(event) {
                if (!mobileMenuButton.contains(event.target) && !mobileMenu.contains(event.target)) {
                    mobileMenu.classList.add('hidden');
                    // Reset all dropdowns
                    const allDropdowns = mobileMenu.querySelectorAll('.mobile-dropdown-content');
                    const allIcons = mobileMenu.querySelectorAll('.mobile-dropdown-toggle svg');
                    allDropdowns.forEach(dropdown => dropdown.classList.add('hidden'));
                    allIcons.forEach(icon => icon.classList.remove('rotate-180'));
                }
            });
            
            // Close mobile menu on window resize (if screen becomes large)
            window.addEventListener('resize', function() {
                if (window.innerWidth >= 1024) { // lg breakpoint
                    mobileMenu.classList.add('hidden');
                    // Reset all dropdowns
                    const allDropdowns = mobileMenu.querySelectorAll('.mobile-dropdown-content');
                    const allIcons = mobileMenu.querySelectorAll('.mobile-dropdown-toggle svg');
                    allDropdowns.forEach(dropdown => dropdown.classList.add('hidden'));
                    allIcons.forEach(icon => icon.classList.remove('rotate-180'));
                }
            });
        } else {
            console.error('Mobile menu elements not found');
        }
    });
    
    // Scroll to top function
    function scrollToTop() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }
</script> 