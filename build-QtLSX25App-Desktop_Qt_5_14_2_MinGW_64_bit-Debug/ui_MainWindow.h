/********************************************************************************
** Form generated from reading UI file 'MainWindow.ui'
**
** Created by: Qt User Interface Compiler version 5.14.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDoubleSpinBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSplitter>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QTableView>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QTreeWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>
#include "myChartView"

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QGridLayout *gridLayout_2;
    QFrame *frameHead;
    QHBoxLayout *horizontalLayout_2;
    QToolButton *toolBtnGenData;
    QToolButton *toolBtnCounting;
    QLabel *label;
    QComboBox *comboTheme;
    QLabel *label_2;
    QComboBox *comboAnimation;
    QSpacerItem *horizontalSpacer;
    QToolButton *toolBtnQuit;
    QSplitter *splitter;
    QFrame *frameData;
    QVBoxLayout *verticalLayout;
    QGroupBox *groupBoxGrade;
    QHBoxLayout *horizontalLayout_3;
    QTableView *tableView;
    QGroupBox *groupBoxCount;
    QGridLayout *gridLayout;
    QTreeWidget *treeWidget;
    QTabWidget *tabWidget;
    QWidget *tabBar;
    QVBoxLayout *verticalLayout_2;
    QWidget *widgetBar;
    QVBoxLayout *verticalLayout_3;
    QFrame *frameBar;
    QHBoxLayout *horizontalLayout_5;
    QPushButton *btnBuildBarChart;
    QPushButton *btnBuildBarChartH;
    QSpacerItem *hSpacerBar;
    QmyChartView *chartViewBar;
    QWidget *tabStackedBar;
    QVBoxLayout *verticalLayout_4;
    QWidget *widgetStackedBar;
    QVBoxLayout *verticalLayout_9;
    QFrame *frameStackedBar;
    QHBoxLayout *horizontalLayout_6;
    QPushButton *btnBuildStackedBar;
    QPushButton *btnBuildStackedBarH;
    QSpacerItem *hSpacerStackedBar;
    QmyChartView *chartViewStackedBar;
    QWidget *tabPercentBar;
    QHBoxLayout *horizontalLayout_4;
    QWidget *widgetPercentBar;
    QVBoxLayout *verticalLayout_10;
    QFrame *framePercentBar;
    QHBoxLayout *horizontalLayout_12;
    QPushButton *btnPercentBar;
    QPushButton *btnPercentBarH;
    QSpacerItem *hSpacerPercentBar;
    QmyChartView *chartViewPercentBar;
    QWidget *tabPieChart;
    QVBoxLayout *verticalLayout_11;
    QWidget *widgetPieBar;
    QVBoxLayout *verticalLayout_8;
    QFrame *framePie;
    QHBoxLayout *horizontalLayout_13;
    QLabel *labelAanlyze;
    QComboBox *comboCourse;
    QPushButton *btnDrawPieChart;
    QLabel *labelHole;
    QDoubleSpinBox *spinHoleSize;
    QLabel *labelPie;
    QDoubleSpinBox *spinPieSize;
    QCheckBox *chkBoxPieLegend;
    QSpacerItem *horizontalSpacer_2;
    QmyChartView *chartViewPie;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(1070, 604);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        gridLayout_2 = new QGridLayout(centralwidget);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        frameHead = new QFrame(centralwidget);
        frameHead->setObjectName(QString::fromUtf8("frameHead"));
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(frameHead->sizePolicy().hasHeightForWidth());
        frameHead->setSizePolicy(sizePolicy);
        frameHead->setFrameShape(QFrame::Panel);
        frameHead->setFrameShadow(QFrame::Raised);
        horizontalLayout_2 = new QHBoxLayout(frameHead);
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        toolBtnGenData = new QToolButton(frameHead);
        toolBtnGenData->setObjectName(QString::fromUtf8("toolBtnGenData"));
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/icons/images/828.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        toolBtnGenData->setIcon(icon);
        toolBtnGenData->setToolButtonStyle(Qt::ToolButtonTextBesideIcon);

        horizontalLayout_2->addWidget(toolBtnGenData);

        toolBtnCounting = new QToolButton(frameHead);
        toolBtnCounting->setObjectName(QString::fromUtf8("toolBtnCounting"));
        QIcon icon1;
        icon1.addFile(QString::fromUtf8(":/icons/images/216.GIF"), QSize(), QIcon::Normal, QIcon::Off);
        toolBtnCounting->setIcon(icon1);
        toolBtnCounting->setToolButtonStyle(Qt::ToolButtonTextBesideIcon);

        horizontalLayout_2->addWidget(toolBtnCounting);

        label = new QLabel(frameHead);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout_2->addWidget(label);

        comboTheme = new QComboBox(frameHead);
        comboTheme->addItem(QString());
        comboTheme->addItem(QString());
        comboTheme->addItem(QString());
        comboTheme->addItem(QString());
        comboTheme->addItem(QString());
        comboTheme->addItem(QString());
        comboTheme->addItem(QString());
        comboTheme->addItem(QString());
        comboTheme->setObjectName(QString::fromUtf8("comboTheme"));

        horizontalLayout_2->addWidget(comboTheme);

        label_2 = new QLabel(frameHead);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        horizontalLayout_2->addWidget(label_2);

        comboAnimation = new QComboBox(frameHead);
        comboAnimation->addItem(QString());
        comboAnimation->addItem(QString());
        comboAnimation->addItem(QString());
        comboAnimation->addItem(QString());
        comboAnimation->setObjectName(QString::fromUtf8("comboAnimation"));

        horizontalLayout_2->addWidget(comboAnimation);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer);

        toolBtnQuit = new QToolButton(frameHead);
        toolBtnQuit->setObjectName(QString::fromUtf8("toolBtnQuit"));
        QIcon icon2;
        icon2.addFile(QString::fromUtf8(":/icons/images/132.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        toolBtnQuit->setIcon(icon2);
        toolBtnQuit->setToolButtonStyle(Qt::ToolButtonTextBesideIcon);

        horizontalLayout_2->addWidget(toolBtnQuit);


        gridLayout_2->addWidget(frameHead, 0, 0, 1, 1);

        splitter = new QSplitter(centralwidget);
        splitter->setObjectName(QString::fromUtf8("splitter"));
        splitter->setOrientation(Qt::Horizontal);
        frameData = new QFrame(splitter);
        frameData->setObjectName(QString::fromUtf8("frameData"));
        frameData->setFrameShape(QFrame::StyledPanel);
        frameData->setFrameShadow(QFrame::Raised);
        verticalLayout = new QVBoxLayout(frameData);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        groupBoxGrade = new QGroupBox(frameData);
        groupBoxGrade->setObjectName(QString::fromUtf8("groupBoxGrade"));
        horizontalLayout_3 = new QHBoxLayout(groupBoxGrade);
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        tableView = new QTableView(groupBoxGrade);
        tableView->setObjectName(QString::fromUtf8("tableView"));

        horizontalLayout_3->addWidget(tableView);


        verticalLayout->addWidget(groupBoxGrade);

        groupBoxCount = new QGroupBox(frameData);
        groupBoxCount->setObjectName(QString::fromUtf8("groupBoxCount"));
        gridLayout = new QGridLayout(groupBoxCount);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        treeWidget = new QTreeWidget(groupBoxCount);
        QTreeWidgetItem *__qtreewidgetitem = new QTreeWidgetItem();
        __qtreewidgetitem->setTextAlignment(0, Qt::AlignCenter);
        treeWidget->setHeaderItem(__qtreewidgetitem);
        new QTreeWidgetItem(treeWidget);
        new QTreeWidgetItem(treeWidget);
        new QTreeWidgetItem(treeWidget);
        new QTreeWidgetItem(treeWidget);
        new QTreeWidgetItem(treeWidget);
        treeWidget->setObjectName(QString::fromUtf8("treeWidget"));
        treeWidget->setEditTriggers(QAbstractItemView::NoEditTriggers);
        treeWidget->header()->setMinimumSectionSize(31);
        treeWidget->header()->setDefaultSectionSize(90);

        gridLayout->addWidget(treeWidget, 0, 0, 1, 1);


        verticalLayout->addWidget(groupBoxCount);

        splitter->addWidget(frameData);
        tabWidget = new QTabWidget(splitter);
        tabWidget->setObjectName(QString::fromUtf8("tabWidget"));
        tabBar = new QWidget();
        tabBar->setObjectName(QString::fromUtf8("tabBar"));
        verticalLayout_2 = new QVBoxLayout(tabBar);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        widgetBar = new QWidget(tabBar);
        widgetBar->setObjectName(QString::fromUtf8("widgetBar"));
        verticalLayout_3 = new QVBoxLayout(widgetBar);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        frameBar = new QFrame(widgetBar);
        frameBar->setObjectName(QString::fromUtf8("frameBar"));
        frameBar->setFrameShape(QFrame::Panel);
        frameBar->setFrameShadow(QFrame::Raised);
        horizontalLayout_5 = new QHBoxLayout(frameBar);
        horizontalLayout_5->setObjectName(QString::fromUtf8("horizontalLayout_5"));
        btnBuildBarChart = new QPushButton(frameBar);
        btnBuildBarChart->setObjectName(QString::fromUtf8("btnBuildBarChart"));

        horizontalLayout_5->addWidget(btnBuildBarChart);

        btnBuildBarChartH = new QPushButton(frameBar);
        btnBuildBarChartH->setObjectName(QString::fromUtf8("btnBuildBarChartH"));

        horizontalLayout_5->addWidget(btnBuildBarChartH);

        hSpacerBar = new QSpacerItem(422, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_5->addItem(hSpacerBar);


        verticalLayout_3->addWidget(frameBar);

        chartViewBar = new QmyChartView(widgetBar);
        chartViewBar->setObjectName(QString::fromUtf8("chartViewBar"));

        verticalLayout_3->addWidget(chartViewBar);


        verticalLayout_2->addWidget(widgetBar);

        QIcon icon3;
        icon3.addFile(QString::fromUtf8(":/icons/images/3.ico"), QSize(), QIcon::Normal, QIcon::Off);
        tabWidget->addTab(tabBar, icon3, QString());
        tabStackedBar = new QWidget();
        tabStackedBar->setObjectName(QString::fromUtf8("tabStackedBar"));
        verticalLayout_4 = new QVBoxLayout(tabStackedBar);
        verticalLayout_4->setObjectName(QString::fromUtf8("verticalLayout_4"));
        widgetStackedBar = new QWidget(tabStackedBar);
        widgetStackedBar->setObjectName(QString::fromUtf8("widgetStackedBar"));
        verticalLayout_9 = new QVBoxLayout(widgetStackedBar);
        verticalLayout_9->setObjectName(QString::fromUtf8("verticalLayout_9"));
        frameStackedBar = new QFrame(widgetStackedBar);
        frameStackedBar->setObjectName(QString::fromUtf8("frameStackedBar"));
        frameStackedBar->setFrameShape(QFrame::Panel);
        frameStackedBar->setFrameShadow(QFrame::Raised);
        horizontalLayout_6 = new QHBoxLayout(frameStackedBar);
        horizontalLayout_6->setObjectName(QString::fromUtf8("horizontalLayout_6"));
        btnBuildStackedBar = new QPushButton(frameStackedBar);
        btnBuildStackedBar->setObjectName(QString::fromUtf8("btnBuildStackedBar"));

        horizontalLayout_6->addWidget(btnBuildStackedBar);

        btnBuildStackedBarH = new QPushButton(frameStackedBar);
        btnBuildStackedBarH->setObjectName(QString::fromUtf8("btnBuildStackedBarH"));

        horizontalLayout_6->addWidget(btnBuildStackedBarH);

        hSpacerStackedBar = new QSpacerItem(225, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_6->addItem(hSpacerStackedBar);


        verticalLayout_9->addWidget(frameStackedBar);

        chartViewStackedBar = new QmyChartView(widgetStackedBar);
        chartViewStackedBar->setObjectName(QString::fromUtf8("chartViewStackedBar"));

        verticalLayout_9->addWidget(chartViewStackedBar);


        verticalLayout_4->addWidget(widgetStackedBar);

        QIcon icon4;
        icon4.addFile(QString::fromUtf8(":/icons/images/280.GIF"), QSize(), QIcon::Normal, QIcon::Off);
        tabWidget->addTab(tabStackedBar, icon4, QString());
        tabPercentBar = new QWidget();
        tabPercentBar->setObjectName(QString::fromUtf8("tabPercentBar"));
        horizontalLayout_4 = new QHBoxLayout(tabPercentBar);
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        widgetPercentBar = new QWidget(tabPercentBar);
        widgetPercentBar->setObjectName(QString::fromUtf8("widgetPercentBar"));
        verticalLayout_10 = new QVBoxLayout(widgetPercentBar);
        verticalLayout_10->setObjectName(QString::fromUtf8("verticalLayout_10"));
        framePercentBar = new QFrame(widgetPercentBar);
        framePercentBar->setObjectName(QString::fromUtf8("framePercentBar"));
        framePercentBar->setFrameShape(QFrame::Panel);
        framePercentBar->setFrameShadow(QFrame::Raised);
        horizontalLayout_12 = new QHBoxLayout(framePercentBar);
        horizontalLayout_12->setObjectName(QString::fromUtf8("horizontalLayout_12"));
        btnPercentBar = new QPushButton(framePercentBar);
        btnPercentBar->setObjectName(QString::fromUtf8("btnPercentBar"));

        horizontalLayout_12->addWidget(btnPercentBar);

        btnPercentBarH = new QPushButton(framePercentBar);
        btnPercentBarH->setObjectName(QString::fromUtf8("btnPercentBarH"));

        horizontalLayout_12->addWidget(btnPercentBarH);

        hSpacerPercentBar = new QSpacerItem(225, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_12->addItem(hSpacerPercentBar);


        verticalLayout_10->addWidget(framePercentBar);

        chartViewPercentBar = new QmyChartView(widgetPercentBar);
        chartViewPercentBar->setObjectName(QString::fromUtf8("chartViewPercentBar"));

        verticalLayout_10->addWidget(chartViewPercentBar);


        horizontalLayout_4->addWidget(widgetPercentBar);

        QIcon icon5;
        icon5.addFile(QString::fromUtf8(":/icons/images/f14.ico"), QSize(), QIcon::Normal, QIcon::Off);
        tabWidget->addTab(tabPercentBar, icon5, QString());
        tabPieChart = new QWidget();
        tabPieChart->setObjectName(QString::fromUtf8("tabPieChart"));
        verticalLayout_11 = new QVBoxLayout(tabPieChart);
        verticalLayout_11->setObjectName(QString::fromUtf8("verticalLayout_11"));
        widgetPieBar = new QWidget(tabPieChart);
        widgetPieBar->setObjectName(QString::fromUtf8("widgetPieBar"));
        verticalLayout_8 = new QVBoxLayout(widgetPieBar);
        verticalLayout_8->setObjectName(QString::fromUtf8("verticalLayout_8"));
        framePie = new QFrame(widgetPieBar);
        framePie->setObjectName(QString::fromUtf8("framePie"));
        framePie->setFrameShape(QFrame::Panel);
        framePie->setFrameShadow(QFrame::Raised);
        horizontalLayout_13 = new QHBoxLayout(framePie);
        horizontalLayout_13->setObjectName(QString::fromUtf8("horizontalLayout_13"));
        labelAanlyze = new QLabel(framePie);
        labelAanlyze->setObjectName(QString::fromUtf8("labelAanlyze"));

        horizontalLayout_13->addWidget(labelAanlyze);

        comboCourse = new QComboBox(framePie);
        comboCourse->addItem(QString());
        comboCourse->addItem(QString());
        comboCourse->addItem(QString());
        comboCourse->addItem(QString());
        comboCourse->addItem(QString());
        comboCourse->setObjectName(QString::fromUtf8("comboCourse"));

        horizontalLayout_13->addWidget(comboCourse);

        btnDrawPieChart = new QPushButton(framePie);
        btnDrawPieChart->setObjectName(QString::fromUtf8("btnDrawPieChart"));

        horizontalLayout_13->addWidget(btnDrawPieChart);

        labelHole = new QLabel(framePie);
        labelHole->setObjectName(QString::fromUtf8("labelHole"));

        horizontalLayout_13->addWidget(labelHole);

        spinHoleSize = new QDoubleSpinBox(framePie);
        spinHoleSize->setObjectName(QString::fromUtf8("spinHoleSize"));
        spinHoleSize->setMaximum(1.000000000000000);
        spinHoleSize->setSingleStep(0.100000000000000);

        horizontalLayout_13->addWidget(spinHoleSize);

        labelPie = new QLabel(framePie);
        labelPie->setObjectName(QString::fromUtf8("labelPie"));

        horizontalLayout_13->addWidget(labelPie);

        spinPieSize = new QDoubleSpinBox(framePie);
        spinPieSize->setObjectName(QString::fromUtf8("spinPieSize"));
        spinPieSize->setMaximum(1.000000000000000);
        spinPieSize->setSingleStep(0.100000000000000);
        spinPieSize->setValue(0.700000000000000);

        horizontalLayout_13->addWidget(spinPieSize);

        chkBoxPieLegend = new QCheckBox(framePie);
        chkBoxPieLegend->setObjectName(QString::fromUtf8("chkBoxPieLegend"));
        chkBoxPieLegend->setChecked(true);

        horizontalLayout_13->addWidget(chkBoxPieLegend);

        horizontalSpacer_2 = new QSpacerItem(13, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_13->addItem(horizontalSpacer_2);


        verticalLayout_8->addWidget(framePie);

        chartViewPie = new QmyChartView(widgetPieBar);
        chartViewPie->setObjectName(QString::fromUtf8("chartViewPie"));

        verticalLayout_8->addWidget(chartViewPie);


        verticalLayout_11->addWidget(widgetPieBar);

        QIcon icon6;
        icon6.addFile(QString::fromUtf8(":/icons/images/43.ico"), QSize(), QIcon::Normal, QIcon::Off);
        tabWidget->addTab(tabPieChart, icon6, QString());
        splitter->addWidget(tabWidget);

        gridLayout_2->addWidget(splitter, 1, 0, 1, 1);

        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 1070, 30));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);
        QObject::connect(toolBtnQuit, SIGNAL(clicked()), MainWindow, SLOT(close()));

        tabWidget->setCurrentIndex(3);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
#if QT_CONFIG(tooltip)
        toolBtnGenData->setToolTip(QCoreApplication::translate("MainWindow", "\351\207\215\346\226\260\347\224\237\346\210\220\346\225\260\346\215\256\345\271\266\347\273\237\350\256\241", nullptr));
#endif // QT_CONFIG(tooltip)
        toolBtnGenData->setText(QCoreApplication::translate("MainWindow", "\351\207\215\346\226\260\347\224\237\346\210\220\346\225\260\346\215\256", nullptr));
#if QT_CONFIG(tooltip)
        toolBtnCounting->setToolTip(QCoreApplication::translate("MainWindow", "\351\207\215\346\226\260\347\273\237\350\256\241", nullptr));
#endif // QT_CONFIG(tooltip)
        toolBtnCounting->setText(QCoreApplication::translate("MainWindow", "\351\207\215\346\226\260\347\273\237\350\256\241", nullptr));
        label->setText(QCoreApplication::translate("MainWindow", "\345\233\276\350\241\250\344\270\273\351\242\230", nullptr));
        comboTheme->setItemText(0, QCoreApplication::translate("MainWindow", "Light", nullptr));
        comboTheme->setItemText(1, QCoreApplication::translate("MainWindow", "BlueCerulean", nullptr));
        comboTheme->setItemText(2, QCoreApplication::translate("MainWindow", "Dark", nullptr));
        comboTheme->setItemText(3, QCoreApplication::translate("MainWindow", "BrownSand", nullptr));
        comboTheme->setItemText(4, QCoreApplication::translate("MainWindow", "BlueNcs", nullptr));
        comboTheme->setItemText(5, QCoreApplication::translate("MainWindow", "HighContrast", nullptr));
        comboTheme->setItemText(6, QCoreApplication::translate("MainWindow", "Bluelcy", nullptr));
        comboTheme->setItemText(7, QCoreApplication::translate("MainWindow", "Qt", nullptr));

        label_2->setText(QCoreApplication::translate("MainWindow", "\345\233\276\350\241\250\345\212\250\347\224\273\346\225\210\346\236\234", nullptr));
        comboAnimation->setItemText(0, QCoreApplication::translate("MainWindow", "NoAnimation", nullptr));
        comboAnimation->setItemText(1, QCoreApplication::translate("MainWindow", "GridAxisAnimations", nullptr));
        comboAnimation->setItemText(2, QCoreApplication::translate("MainWindow", "SeriesAnimations", nullptr));
        comboAnimation->setItemText(3, QCoreApplication::translate("MainWindow", "AllAnimations", nullptr));

#if QT_CONFIG(tooltip)
        toolBtnQuit->setToolTip(QCoreApplication::translate("MainWindow", "\351\200\200\345\207\272", nullptr));
#endif // QT_CONFIG(tooltip)
        toolBtnQuit->setText(QCoreApplication::translate("MainWindow", "\351\200\200\345\207\272", nullptr));
        groupBoxGrade->setTitle(QCoreApplication::translate("MainWindow", "\345\216\237\345\247\213\345\210\206\346\225\260", nullptr));
        groupBoxCount->setTitle(QCoreApplication::translate("MainWindow", "\344\272\272\346\225\260\347\273\237\350\256\241", nullptr));
        QTreeWidgetItem *___qtreewidgetitem = treeWidget->headerItem();
        ___qtreewidgetitem->setText(5, QCoreApplication::translate("MainWindow", "\351\255\205\345\212\233", nullptr));
        ___qtreewidgetitem->setText(4, QCoreApplication::translate("MainWindow", "\346\224\277\346\262\273", nullptr));
        ___qtreewidgetitem->setText(3, QCoreApplication::translate("MainWindow", "\346\231\272\345\212\233", nullptr));
        ___qtreewidgetitem->setText(2, QCoreApplication::translate("MainWindow", "\346\255\246\345\212\233", nullptr));
        ___qtreewidgetitem->setText(1, QCoreApplication::translate("MainWindow", "\347\273\237\345\270\205", nullptr));
        ___qtreewidgetitem->setText(0, QCoreApplication::translate("MainWindow", "\345\210\206\346\225\260\346\256\265", nullptr));

        const bool __sortingEnabled = treeWidget->isSortingEnabled();
        treeWidget->setSortingEnabled(false);
        QTreeWidgetItem *___qtreewidgetitem1 = treeWidget->topLevelItem(0);
        ___qtreewidgetitem1->setText(0, QCoreApplication::translate("MainWindow", "0~59", nullptr));
        QTreeWidgetItem *___qtreewidgetitem2 = treeWidget->topLevelItem(1);
        ___qtreewidgetitem2->setText(0, QCoreApplication::translate("MainWindow", "60~69", nullptr));
        QTreeWidgetItem *___qtreewidgetitem3 = treeWidget->topLevelItem(2);
        ___qtreewidgetitem3->setText(0, QCoreApplication::translate("MainWindow", "70~79", nullptr));
        QTreeWidgetItem *___qtreewidgetitem4 = treeWidget->topLevelItem(3);
        ___qtreewidgetitem4->setText(0, QCoreApplication::translate("MainWindow", "80~89", nullptr));
        QTreeWidgetItem *___qtreewidgetitem5 = treeWidget->topLevelItem(4);
        ___qtreewidgetitem5->setText(0, QCoreApplication::translate("MainWindow", "90~100", nullptr));
        treeWidget->setSortingEnabled(__sortingEnabled);

        btnBuildBarChart->setText(QCoreApplication::translate("MainWindow", "\347\273\230\345\210\266\346\237\261\347\212\266\345\233\276", nullptr));
        btnBuildBarChartH->setText(QCoreApplication::translate("MainWindow", "\347\273\230\345\210\266\346\260\264\345\271\263\346\237\261\347\212\266\345\233\276", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tabBar), QCoreApplication::translate("MainWindow", "\346\237\261\347\212\266\345\233\276", nullptr));
        btnBuildStackedBar->setText(QCoreApplication::translate("MainWindow", "\347\273\230\345\210\266\346\237\261\347\212\266\345\233\276", nullptr));
        btnBuildStackedBarH->setText(QCoreApplication::translate("MainWindow", "\347\273\230\345\210\266\346\260\264\345\271\263\346\237\261\347\212\266\345\233\276", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tabStackedBar), QCoreApplication::translate("MainWindow", "\345\240\206\345\217\240\346\237\261\347\212\266\345\233\276", nullptr));
        btnPercentBar->setText(QCoreApplication::translate("MainWindow", "\347\273\230\345\210\266\346\237\261\347\212\266\345\233\276", nullptr));
        btnPercentBarH->setText(QCoreApplication::translate("MainWindow", "\347\273\230\345\210\266\346\260\264\345\271\263\346\237\261\347\212\266\345\233\276", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tabPercentBar), QCoreApplication::translate("MainWindow", "\347\231\276\345\210\206\346\257\224\346\237\261\347\212\266\345\233\276", nullptr));
        labelAanlyze->setText(QCoreApplication::translate("MainWindow", "\346\225\260\346\215\256\345\210\206\346\236\220", nullptr));
        comboCourse->setItemText(0, QCoreApplication::translate("MainWindow", "\347\273\237\345\270\205", nullptr));
        comboCourse->setItemText(1, QCoreApplication::translate("MainWindow", "\346\255\246\345\212\233", nullptr));
        comboCourse->setItemText(2, QCoreApplication::translate("MainWindow", "\346\231\272\345\212\233", nullptr));
        comboCourse->setItemText(3, QCoreApplication::translate("MainWindow", "\346\224\277\346\262\273", nullptr));
        comboCourse->setItemText(4, QCoreApplication::translate("MainWindow", "\351\255\205\345\212\233", nullptr));

        btnDrawPieChart->setText(QCoreApplication::translate("MainWindow", "\347\273\230\345\210\266\351\245\274\345\233\276", nullptr));
        labelHole->setText(QCoreApplication::translate("MainWindow", "HoleSize", nullptr));
        labelPie->setText(QCoreApplication::translate("MainWindow", "PieSize", nullptr));
        chkBoxPieLegend->setText(QCoreApplication::translate("MainWindow", "\346\230\276\347\244\272\345\233\276\344\276\213", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tabPieChart), QCoreApplication::translate("MainWindow", "\351\245\274\345\233\276", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
