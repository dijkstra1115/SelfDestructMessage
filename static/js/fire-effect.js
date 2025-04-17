// 火焰效果腳本

// 創建灰燼飄落效果
function createAshes() {
    const container = document.querySelector('.container');
    if (!container) return;
    
    for (let i = 0; i < 50; i++) {
        const ash = document.createElement('div');
        ash.classList.add('ash');
        
        // 隨機位置
        const left = Math.random() * 100;
        
        ash.style.left = `${left}%`;
        ash.style.top = '-10px';
        
        container.appendChild(ash);
        
        // 隨機動畫
        const delay = Math.random() * 5;
        const duration = 3 + Math.random() * 5;
        
        ash.style.animation = `fall ${duration}s ease-in ${delay}s forwards`;
    }
}

// 創建星空背景
function createStars() {
    const starsContainer = document.querySelector('.stars');
    if (!starsContainer) return;
    
    const starsCount = 100;
    
    for (let i = 0; i < starsCount; i++) {
        const star = document.createElement('div');
        star.classList.add('star');
        
        // 隨機位置
        const top = Math.random() * 100;
        const left = Math.random() * 100;
        
        star.style.top = `${top}%`;
        star.style.left = `${left}%`;
        
        // 隨機大小
        const size = Math.random() * 3;
        star.style.width = `${size}px`;
        star.style.height = `${size}px`;
        
        // 隨機動畫延遲
        const delay = Math.random() * 5;
        star.style.animationDelay = `${delay}s`;
        
        starsContainer.appendChild(star);
    }
}

// 頁面加載時初始化效果
window.addEventListener('load', function() {
    createAshes();
    createStars();
}); 