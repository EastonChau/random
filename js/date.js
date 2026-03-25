// date
const DateObj = new Date();
const dateStr = DateObj.toLocaleDateString('en-US', { 
    year: 'numeric', 
    month: 'long', 
    day: 'numeric' 
});

function getDate() {
    const today = new Date();
    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, '0');
    const day = String(today.getDate()).padStart(2, '0');
    const dateString = `${year}${month}${day}`;
    return Number(dataString);
}

document.querySelector('.date-display').textContent = `Date: ${dateStr}`;
