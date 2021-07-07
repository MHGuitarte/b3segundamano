const modal = document.querySelector('#accessModal');
const tabContents = document.querySelectorAll('.tab-content');
const tabButtons = document.querySelectorAll('.tab-button');

//Abrir modal de Acceso/Registro
function openAccessModal(hasAccount) {
    modal.style.display = "block";

    if (hasAccount) {
        openTab('login-tab', 'tab-login-button');
    } else {
        openTab('register-tab', 'tab-register-button');
    }
}

function openTab(tabId, tabButton) {

    const selectedTab = document.getElementById(tabId);
    const selectedButton = document.getElementById(tabButton);

    for (tab of tabContents) {
        tab.style.display = "none";
    }

    for (button of tabButtons) {
        button.classList.remove('w3-bottombar');
        button.classList.remove('border-primary');
    }

    selectedButton.classList.add('w3-bottombar');
    selectedButton.classList.add('w3-border-pink');
    selectedTab.style.display = "block";

}

function closeModal() {
    modal.style.display = "none";
}