using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace animal_checker
{
    /// <summary>
    /// MainWindow.xaml 的交互逻辑
    /// </summary>
    public partial class MainWindow : Window
    {
        /**
         * 红方：象（8）、狮（7）、虎（6）、豹（5）、狼（4）、狗（3）、猫（2）、鼠（1）
         * 黑方：象（-8）、狮（-7）、虎（-6）、豹（-5）、狼（-4）、狗（-3）、猫（-2）、鼠（-1）
         * 
         * game 通过保存以上不同的数据来记录游戏的进行
         * 
         */
        int [,] game = new int[9, 7];
        List<TextBlock> Red = new List<TextBlock>();
        List<TextBlock> Black = new List<TextBlock>();
        List<Rectangle> target = new List<Rectangle>();
        //List<Rectangle> blocks = new List<Rectangle>();
        Rectangle[,] blocks = new Rectangle[9, 7];
        int targetX = 0, targetY = 0, _targetX, _targetY;
        int flag = 0; // flag 表示敲回车的次数，2次后置为0
        int isSelect = 0, targetNum;
        int isNext = 0;

        public MainWindow()
        {
            InitializeComponent();
            initChessBoard();
            initChessPieces();
            initGame();
            initTarget();
        }

        public void initChessBoard() {
            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 7; j++) {
                    Rectangle block = getBlock(j, i);
                    chessBoard.Children.Add(block);
                    blocks[i, j] = block;
                    Canvas.SetLeft(block, j * 50);
                    Canvas.SetTop(block, i * 50);
                }
            }
        }

        public void initGame() {
            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 7; j++) {
                    if (i == 0 && j == 0) {
                        game[i, j] = -7;
                    }
                    else if (i == 8 && j == 6) {
                        game[i, j] = 7; 
                    }
                    else if (i == 0 && j == 6) {
                        game[i, j] = -6;
                    }
                    else if (i == 8 && j == 0) {
                        game[i, j] = 6;
                    }
                    else if (i == 1 && j == 1) {
                        game[i, j] = -3;
                    }
                    else if (i == 7 && j == 5) {
                        game[i, j] = 3;
                    }
                    else if (i == 1 && j == 5) {
                        game[i, j] = -2;
                    }
                    else if (i == 7 && j == 1) {
                        game[i, j] = 2;
                    }
                    else if (i == 2 && j == 0) {
                        game[i, j] = -1;
                    }
                    else if (i == 6 && j == 6) {
                        game[i, j] = 1;
                    }
                    else if (i == 2 && j == 2) {
                        game[i, j] = -5;
                    }
                    else if (i == 6 && j == 4) {
                        game[i, j] = 5;
                    }
                    else if (i == 2 && j == 4) {
                        game[i, j] = -4;
                    }
                    else if (i == 6 && j == 2) {
                        game[i, j] = 4;
                    }
                    else if (i == 2 && j == 6) {
                        game[i, j] = -8;
                    }
                    else if (i == 6 && j == 0) {
                        game[i, j] = 8;
                    }
                    else {
                        game[i, j] = 0;
                    }
                }
            }

            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 7; j++) {
                    switch (game[i, j]) { 
                        case 1:
                            Canvas.SetLeft(Red[0], 50 * j);
                            Canvas.SetTop(Red[0], 50 * i);
                            chessBoard.Children.Add(Red[0]);
                            break;
                        case -1:
                            Canvas.SetLeft(Black[0], 50 * j);
                            Canvas.SetTop(Black[0], 50 * i);
                            chessBoard.Children.Add(Black[0]);
                            break;
                        case 2:
                            Canvas.SetLeft(Red[1], 50 * j);
                            Canvas.SetTop(Red[1], 50 * i);
                            chessBoard.Children.Add(Red[1]);
                            break;
                        case -2:
                            Canvas.SetLeft(Black[1], 50 * j);
                            Canvas.SetTop(Black[1], 50 * i);
                            chessBoard.Children.Add(Black[1]);
                            break;
                        case 3:
                            Canvas.SetLeft(Red[2], 50 * j);
                            Canvas.SetTop(Red[2], 50 * i);
                            chessBoard.Children.Add(Red[2]);
                            break;
                        case -3:
                            Canvas.SetLeft(Black[2], 50 * j);
                            Canvas.SetTop(Black[2], 50 * i);
                            chessBoard.Children.Add(Black[2]);
                            break;
                        case 4:
                            Canvas.SetLeft(Red[3], 50 * j);
                            Canvas.SetTop(Red[3], 50 * i);
                            chessBoard.Children.Add(Red[3]);
                            break;
                        case -4:
                            Canvas.SetLeft(Black[3], 50 * j);
                            Canvas.SetTop(Black[3], 50 * i);
                            chessBoard.Children.Add(Black[3]);
                            break;
                        case 5:
                            Canvas.SetLeft(Red[4], 50 * j);
                            Canvas.SetTop(Red[4], 50 * i);
                            chessBoard.Children.Add(Red[4]);
                            break;
                        case -5:
                            Canvas.SetLeft(Black[4], 50 * j);
                            Canvas.SetTop(Black[4], 50 * i);
                            chessBoard.Children.Add(Black[4]);
                            break;
                        case 6:
                            Canvas.SetLeft(Red[5], 50 * j);
                            Canvas.SetTop(Red[5], 50 * i);
                            chessBoard.Children.Add(Red[5]);
                            break;
                        case -6:
                            Canvas.SetLeft(Black[5], 50 * j);
                            Canvas.SetTop(Black[5], 50 * i);
                            chessBoard.Children.Add(Black[5]);
                            break;
                        case 7:
                            Canvas.SetLeft(Red[6], 50 * j);
                            Canvas.SetTop(Red[6], 50 * i);
                            chessBoard.Children.Add(Red[6]);
                            break;
                        case -7:
                            Canvas.SetLeft(Black[6], 50 * j);
                            Canvas.SetTop(Black[6], 50 * i);
                            chessBoard.Children.Add(Black[6]);
                            break;
                        case 8:
                            Canvas.SetLeft(Red[7], 50 * j);
                            Canvas.SetTop(Red[7], 50 * i);
                            chessBoard.Children.Add(Red[7]);
                            break;
                        case -8:
                            Canvas.SetLeft(Black[7], 50 * j);
                            Canvas.SetTop(Black[7], 50 * i);
                            chessBoard.Children.Add(Black[7]);
                            break;
                    }
                }
            }

        }
        public void initChessPieces() {
            for (int i = 0; i < 8; i++) {
                Red.Add(getChess(0));
                Black.Add(getChess(1));
            }
            for (int i = 0; i < 8; i++) {
                switch (i) { 
                    case 0:
                        Red[i].Text = "鼠";
                        Black[i].Text = "鼠";
                        break;
                    case 1:
                        Red[i].Text = "猫";
                        Black[i].Text = "猫";
                        break;
                    case 2:
                        Red[i].Text = "狗";
                        Black[i].Text = "狗";
                        break;
                    case 3:
                        Red[i].Text = "狼";
                        Black[i].Text = "狼";
                        break;
                    case 4:
                        Red[i].Text = "豹";
                        Black[i].Text = "豹";
                        break;
                    case 5:
                        Red[i].Text = "虎";
                        Black[i].Text = "虎";
                        break;
                    case 6:
                        Red[i].Text = "狮";
                        Black[i].Text = "狮";
                        break;
                    case 7:
                        Red[i].Text = "象";
                        Black[i].Text = "象";
                        break;
                }
            }
        }

        public Rectangle getBlock(int x, int y) {
            Rectangle block = new Rectangle();
            block.Height = 48;
            block.Width = 48;
            block.RadiusX = 5;
            block.RadiusY = 5;
            if ((((x == 2 || x == 4) && (y == 0 || y == 8)) ||
                (x == 3 && (y == 1 || y == 7)))) {
                block.Fill = new SolidColorBrush(Colors.Red);
            } 
            else if ((x == 3) && (y == 0 || y == 8)) {
                block.Fill = new SolidColorBrush(Colors.Goldenrod);
            }
            else if (((x >= 1 && x <= 2) && (y >= 3 && y <= 5)) ||
                        (x >= 4 && x <= 5) && (y >= 3 && y <= 5)) {
                block.Fill = new SolidColorBrush(Colors.CadetBlue);
            }
            else {
                block.Fill = new SolidColorBrush(Colors.Gray);
            }
            return block;
        }

        void initTarget() {
            Rectangle rect = getTargetBlock();
            target.Clear();
            target.Add(rect);
            chessBoard.Children.Add(target[0]);
            Canvas.SetTop(target[0], targetY * 50);
            Canvas.SetLeft(target[0], targetX * 50);   
        }

        Rectangle getTargetBlock() {
            Rectangle rect = new Rectangle();
            rect.Width = 50;
            rect.Height = 50;
            rect.RadiusX = 5;
            rect.RadiusY = 5;
            rect.StrokeThickness = isSelect == 1 ? 4:2;
            rect.Stroke = new SolidColorBrush(Colors.Blue);
            return rect;
        }

        private void chessBoard_PreviewKeyDown(object sender, KeyEventArgs e)
        {
            
            
            switch (e.Key) { 
                case Key.Up:
                    targetUp();
                    break;
                case Key.Down:
                    targetDown();
                    break;
                case Key.Left:
                    targetLeft();
                    break;
                case Key.Right:
                    targetRight();
                    break;
                    
                case Key.Enter:
                    flag += 1;
                    switch (flag)
                    {
                        case 1:
                            SelectPieces();
                            nextStep();
                            break;
                        case 2:
                            Boolean isFight =  fight();
                            if (!isFight) {
                                movePieces();
                            }
                            
                            //initChessBoard();
                            
                            resetChessBroad();
                            break;
                    }
                    break;
            }
            

            
            chessBoard.Children.Remove(target[0]);
            initTarget();
            
        }

        public void targetUp() {
            if (targetY == 0) {
                return;
            }
            targetY -= 1;
        }

        public void targetDown() {
            if (targetY == 8) {
                return;
            }
            targetY += 1;
        }

        public void targetLeft() {
            if (targetX == 0) {
                return;
            }
            targetX -= 1;
        }

        public void targetRight() {
            if (targetX == 6) {
                return;
            }
            targetX += 1;
        }

        public void SelectPieces() {
            if (game[targetY, targetX] != 0) {
                targetNum = game[targetY, targetX];
                _targetX = targetX;
                _targetY = targetY;
                isSelect = 1;
                isNext = 1;
            }
        }

        public void movePieces() {
            flag = 0; 
            if (isSelect != 1) {
                return;
            }
            switch (targetNum) { 
                case 1:
                    chessBoard.Children.Remove(Red[0]);
                    Red[0] = getChess(0);
                    Red[0].Text = "鼠";
                    Canvas.SetLeft(Red[0], targetX * 50);
                    Canvas.SetTop(Red[0], targetY * 50);
                    chessBoard.Children.Add(Red[0]);
                    game[targetY, targetX] = 1;
                    game[_targetY, _targetX] = 0;
                    break;
                case -1:
                    chessBoard.Children.Remove(Black[0]);
                    Black[0] = getChess(1);
                    Black[0].Text = "鼠";
                    Canvas.SetLeft(Black[0], targetX * 50);
                    Canvas.SetTop(Black[0], targetY * 50);
                    chessBoard.Children.Add(Black[0]);
                    game[targetY, targetX] = -1;
                    game[_targetY, _targetX] = 0;
                    break;
                case 2:
                    chessBoard.Children.Remove(Red[1]);
                    Red[1] = getChess(0);
                    Red[1].Text = "猫";
                    Canvas.SetLeft(Red[1], targetX * 50);
                    Canvas.SetTop(Red[1], targetY * 50);
                    chessBoard.Children.Add(Red[1]);
                    game[targetY, targetX] = 2;
                    game[_targetY, _targetX] = 0;
                    break;
                case -2:
                    chessBoard.Children.Remove(Black[1]);
                    Black[1] = getChess(1);
                    Black[1].Text = "猫";
                    Canvas.SetLeft(Black[1], targetX * 50);
                    Canvas.SetTop(Black[1], targetY * 50);
                    chessBoard.Children.Add(Black[1]);
                    game[targetY, targetX] = -2;
                    game[_targetY, _targetX] = 0;
                    break;
                case 3:
                    chessBoard.Children.Remove(Red[2]);
                    Red[2] = getChess(0);
                    Red[2].Text = "狗";
                    Canvas.SetLeft(Red[2], targetX * 50);
                    Canvas.SetTop(Red[2], targetY * 50);
                    chessBoard.Children.Add(Red[2]);
                    game[targetY, targetX] = 3;
                    game[_targetY, _targetX] = 0;
                    break;
                case -3:
                    chessBoard.Children.Remove(Black[2]);
                    Black[2] = getChess(1);
                    Black[2].Text = "狗";
                    Canvas.SetLeft(Black[2], targetX * 50);
                    Canvas.SetTop(Black[2], targetY * 50);
                    chessBoard.Children.Add(Black[2]);
                    game[targetY, targetX] = -3;
                    game[_targetY, _targetX] = 0;
                    break;
                case 4:
                    chessBoard.Children.Remove(Red[3]);
                    Red[3] = getChess(0);
                    Red[3].Text = "狼";
                    Canvas.SetLeft(Red[3], targetX * 50);
                    Canvas.SetTop(Red[3], targetY * 50);
                    chessBoard.Children.Add(Red[3]);
                    game[targetY, targetX] = 4;
                    game[_targetY, _targetX] = 0;
                    break;
                case -4:
                    chessBoard.Children.Remove(Black[3]);
                    Black[3] = getChess(1);
                    Black[3].Text = "狼";
                    Canvas.SetLeft(Black[3], targetX * 50);
                    Canvas.SetTop(Black[3], targetY * 50);
                    chessBoard.Children.Add(Black[3]);
                    game[targetY, targetX] = -4;
                    game[_targetY, _targetX] = 0;
                    break;
                case 5:
                    chessBoard.Children.Remove(Red[4]);
                    Red[4] = getChess(0);
                    Red[4].Text = "豹";
                    Canvas.SetLeft(Red[4], targetX * 50);
                    Canvas.SetTop(Red[4], targetY * 50);
                    chessBoard.Children.Add(Red[4]);
                    game[targetY, targetX] = 5;
                    game[_targetY, _targetX] = 0;
                    break;
                case -5:
                    chessBoard.Children.Remove(Black[4]);
                    Black[4] = getChess(1);
                    Black[4].Text = "豹";
                    Canvas.SetLeft(Black[4], targetX * 50);
                    Canvas.SetTop(Black[4], targetY * 50);
                    chessBoard.Children.Add(Black[4]);
                    game[targetY, targetX] = -5;
                    game[_targetY, _targetX] = 0;
                    break;
                case 6:
                    chessBoard.Children.Remove(Red[5]);
                    Red[5] = getChess(0);
                    Red[5].Text = "虎";
                    Canvas.SetLeft(Red[5], targetX * 50);
                    Canvas.SetTop(Red[5], targetY * 50);
                    chessBoard.Children.Add(Red[5]);
                    game[targetY, targetX] = 6;
                    game[_targetY, _targetX] = 0;
                    break;
                case -6:
                    chessBoard.Children.Remove(Black[5]);
                    Black[5] = getChess(1);
                    Black[5].Text = "虎";
                    Canvas.SetLeft(Black[5], targetX * 50);
                    Canvas.SetTop(Black[5], targetY * 50);
                    chessBoard.Children.Add(Black[5]);
                    game[targetY, targetX] = -6;
                    game[_targetY, _targetX] = 0;
                    break;
                case 7:
                    chessBoard.Children.Remove(Red[6]);
                    Red[6] = getChess(0);
                    Red[6].Text = "狮";
                    Canvas.SetLeft(Red[6], targetX * 50);
                    Canvas.SetTop(Red[6], targetY * 50);
                    chessBoard.Children.Add(Red[6]);
                    game[targetY, targetX] = 7;
                    game[_targetY, _targetX] = 0;
                    break;
                case -7:
                    chessBoard.Children.Remove(Black[6]);
                    Black[6] = getChess(1);
                    Black[6].Text = "狮";
                    Canvas.SetLeft(Black[6], targetX * 50);
                    Canvas.SetTop(Black[6], targetY * 50);
                    chessBoard.Children.Add(Black[6]);
                    game[targetY, targetX] = -7;
                    game[_targetY, _targetX] = 0;
                    break;
                case 8:
                    chessBoard.Children.Remove(Red[7]);
                    Red[7] = getChess(0);
                    Red[7].Text = "象";
                    Canvas.SetLeft(Red[7], targetX * 50);
                    Canvas.SetTop(Red[7], targetY * 50);
                    chessBoard.Children.Add(Red[7]);
                    game[targetY, targetX] = 8;
                    game[_targetY, _targetX] = 0;
                    break;
                case -8:
                    chessBoard.Children.Remove(Black[7]);
                    Black[7] = getChess(1);
                    Black[7].Text = "象";
                    Canvas.SetLeft(Black[7], targetX * 50);
                    Canvas.SetTop(Black[7], targetY * 50);
                    chessBoard.Children.Add(Black[7]);
                    game[targetY, targetX] = -8;
                    game[_targetY, _targetX] = 0;
                    break;
            }
            isSelect = 0;
        }

        // key = 0 ,红棋，key = 1,黑棋
        public TextBlock getChess(int key) {
            TextBlock chess = new TextBlock();
            chess.Width = 45;
            chess.Height = 45;
            chess.FontSize = 32;
            chess.TextAlignment = TextAlignment.Center;
            if (key == 0) {
                chess.Foreground = new SolidColorBrush(Colors.Brown);
            } else if (key == 1) {
                chess.Foreground = new SolidColorBrush(Colors.Black);
            }    
            return chess;
        }

        public void nextStep() {
            if (isNext != 1) {
                return;
            }
            isNext = 0;
            if (targetY - 1 >= 0 && game[targetY - 1, targetX] == 0) {
                blocks[targetY - 1, targetX].Fill = new SolidColorBrush(Colors.GreenYellow);
            }
            if (targetY + 1 <= 8 && game[targetY + 1, targetX] == 0) {
                blocks[targetY + 1, targetX].Fill = new SolidColorBrush(Colors.GreenYellow);
            }
            if (targetX - 1 >= 0 && game[targetY, targetX - 1] == 0) {
                blocks[targetY, targetX - 1].Fill = new SolidColorBrush(Colors.GreenYellow);
            }
            if (targetX + 1 <= 6 && game[targetY,  targetX + 1] == 0) {
                blocks[targetY, targetX + 1].Fill = new SolidColorBrush(Colors.GreenYellow);
            }
        }

        public void resetChessBroad() {
            for (int y = 0; y < 9; y++) {
                for (int x = 0; x < 7; x++) {
                    if ((((x == 2 || x == 4) && (y == 0 || y == 8)) ||
                (x == 3 && (y == 1 || y == 7))))
                    {
                        blocks[y, x].Fill = new SolidColorBrush(Colors.Red);
                    }
                    else if ((x == 3) && (y == 0 || y == 8))
                    {
                        blocks[y, x].Fill = new SolidColorBrush(Colors.Goldenrod);
                    }
                    else if (((x >= 1 && x <= 2) && (y >= 3 && y <= 5)) ||
                                (x >= 4 && x <= 5) && (y >= 3 && y <= 5))
                    {
                        blocks[y, x].Fill = new SolidColorBrush(Colors.CadetBlue);
                    }
                    else
                    {
                        blocks[y, x].Fill = new SolidColorBrush(Colors.Gray);
                    }
                }
            }
        }
        public Boolean fight() {
            int _targetNum = game[targetY, targetX];
            //int blackIndex = game[_targetY, _targetX];
            
            if ((_targetNum + targetNum) == 0) {
                chessBoard.Children.Remove(Red[Math.Abs(targetNum) - 1]);
                chessBoard.Children.Remove(Black[Math.Abs(targetNum) - 1]);
                game[targetY, targetX] = 0;
                game[_targetY, _targetX] = 0;
                flag = 0;
                return true;
            }
            else if (Math.Abs(targetNum) > Math.Abs(_targetNum) 
                && Math.Abs(_targetNum) > 0) {
                if (targetNum > 0) {
                    chessBoard.Children.Remove(Black[Math.Abs(_targetNum) - 1]);

                    chessBoard.Children.Remove(Red[Math.Abs(targetNum) - 1]);
                    Canvas.SetLeft(Red[Math.Abs(targetNum) - 1], targetX * 50);
                    Canvas.SetTop(Red[Math.Abs(targetNum) - 1], targetY * 50);
                    chessBoard.Children.Add(Red[Math.Abs(targetNum) - 1]);
                    flag = 0;
                    game[_targetY, _targetX] = 0;
                    game[targetY, targetX] = targetNum;
                    return true;
                }
                else if (targetNum < 0) {
                    chessBoard.Children.Remove(Red[Math.Abs(_targetNum) - 1]);
                    chessBoard.Children.Remove(Black[Math.Abs(targetNum) - 1]);
                    Canvas.SetLeft(Black[Math.Abs(targetNum) - 1], targetX * 50);
                    Canvas.SetTop(Black[Math.Abs(targetNum) - 1], targetY * 50);
                    chessBoard.Children.Add(Black[Math.Abs(targetNum) - 1]);
                    flag = 0;
                    game[_targetY, _targetX] = 0;
                    game[targetY, targetX] = targetNum;
                    return true;
                }
                
            }
            return false;
        }
    }
}
