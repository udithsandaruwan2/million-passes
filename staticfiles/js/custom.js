document.addEventListener("DOMContentLoaded", function() {
    const alerts = document.querySelectorAll('.alert');
    
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.classList.add('fade-out');
            setTimeout(() => {
                alert.remove();
            }, 750); // Wait for the fade-out animation to finish before removing the element
        }, 2000); // 2 seconds delay before fading out
    });

    document.querySelectorAll('.close').forEach(closeButton => {
        closeButton.addEventListener('click', function() {
            const alert = this.parentElement;
            alert.classList.add('fade-out');
            setTimeout(() => {
                alert.remove();
            }, 750); // Wait for the fade-out animation to finish before removing the element
        });
    });
});
