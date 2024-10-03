// script.js
let board = ["", "", "", "", "", "", "", "", ""];
let currentPlayer = "X";
let gameActive = true;
let playerXName = "Player X";
let playerOName = "Player O";

const winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
];

const statusDisplay = document.getElementById("status");

// Start the game and hide the welcome screen
function startGame() {
    playerXName = document.getElementById("player-x-name").value || "Player X";
    playerOName = document.getElementById("player-o-name").value || "Player O";
    document.getElementById("welcome-screen").style.display = "none";
    document.getElementById("game-screen").style.display = "block";
    updateStatus();
}

// Handle cell click
function handleClick(index) {
    if (board[index] === "" && gameActive) {
        board[index] = currentPlayer;
        document.getElementById(`cell-${index}`).textContent = currentPlayer;
        checkWinner();
        switchPlayer();
    }
}

// Switch player turn
function switchPlayer() {
    currentPlayer = currentPlayer === "X" ? "O" : "X";
    updateStatus();
}

// Update status message with player names
function updateStatus() {
    statusDisplay.textContent = `It's ${currentPlayer === "X" ? playerXName : playerOName}'s turn.`;
}

// Check for winner or draw
function checkWinner() {
    let roundWon = false;
    for (let i = 0; i < winningConditions.length; i++) {
        const winCondition = winningConditions[i];
        let a = board[winCondition[0]];
        let b = board[winCondition[1]];
        let c = board[winCondition[2]];

        if (a === "" || b === "" || c === "") {
            continue;
        }
        if (a === b && b === c) {
            roundWon = true;
            break;
        }
    }

    if (roundWon) {
        statusDisplay.textContent = `🎉 ${currentPlayer === "X" ? playerXName : playerOName} wins! 🎉`;
        gameActive = false;
        return;
    }

    if (!board.includes("")) {
        statusDisplay.textContent = "It's a draw!";
        gameActive = false;
    }
}

// Reset the game
function resetGame() {
    board = ["", "", "", "", "", "", "", "", ""];
    currentPlayer = "X";
    gameActive = true;
    document.querySelectorAll(".cell").forEach(cell => (cell.textContent = ""));
    updateStatus();
}
