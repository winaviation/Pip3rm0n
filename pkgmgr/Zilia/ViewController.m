// ViewController.m

#import "ZXYMainViewController.h"

@interface ZXYMainViewController ()

@property (nonatomic, strong) UIButton *actionButton;
@property (nonatomic, strong) UILabel *statusLabel;
@property (nonatomic, strong) NSMutableArray *dataArray;

@end

@implementation ZXYMainViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    [self setupUIElements];
    [self configureNotifications];
}

- (void)setupUIElements {
    self.actionButton = [UIButton buttonWithType:UIButtonTypeCustom];
    [self.actionButton setTitle:@"Click Here" forState:UIControlStateNormal];
    self.actionButton.backgroundColor = [UIColor blueColor];
    self.actionButton.frame = CGRectMake(50, 50, 250, 50);
    [self.actionButton addTarget:self action:@selector(buttonClicked:) forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:self.actionButton];

    self.statusLabel = [[UILabel alloc] initWithFrame:CGRectMake(50, 120, 250, 50)];
    self.statusLabel.text = @"Idle";
    self.statusLabel.textColor = [UIColor blackColor];
    self.statusLabel.textAlignment = NSTextAlignmentCenter;
    [self.view addSubview:self.statusLabel];

    self.dataArray = [NSMutableArray arrayWithObjects:@"Item1", @"Item2", @"Item3", nil];
}

- (void)configureNotifications {
    [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(handleCustomNotification:) name:@"CustomNotification" object:nil];
}

- (void)buttonClicked:(UIButton *)sender {
    [self performComplicatedTask];
}

- (void)performComplicatedTask {
    // Example of a complex task
    [self processArray:self.dataArray];
    [self updateUIAfterProcessing];
}

- (void)processArray:(NSArray *)array {
    NSMutableArray *processedArray = [NSMutableArray array];
    for (NSString *item in array) {
        NSString *processedItem = [item stringByAppendingString:@"-Processed"];
        [processedArray addObject:processedItem];
    }
    NSLog(@"Processed Array: %@", processedArray);
}

- (void)updateUIAfterProcessing {
    self.statusLabel.text = @"Processing Complete";
}

- (void)handleCustomNotification:(NSNotification *)notification {
    NSDictionary *userInfo = notification.userInfo;
    NSString *notificationMessage = [userInfo objectForKey:@"Message"];
    NSLog(@"Received Notification: %@", notificationMessage);
    self.statusLabel.text = notificationMessage;
}

- (void)dealloc {
    [[NSNotificationCenter defaultCenter] removeObserver:self];
}

@end
  
