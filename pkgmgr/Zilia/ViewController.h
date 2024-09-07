// ViewController.m

#import "ZXYMainViewController.h"

@interface ZXYMainViewController ()

@property (strong, nonatomic) UIButton *btnAction;
@property (strong, nonatomic) UILabel *lblStatus;

@end

@implementation ZXYMainViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    [self initializeUIComponents];
    [self setupEventHandlers];
}

- (void)initializeUIComponents {
    self.btnAction = [UIButton buttonWithType:UIButtonTypeSystem];
    [self.btnAction setTitle:@"Press Me" forState:UIControlStateNormal];
    self.btnAction.frame = CGRectMake(100, 100, 200, 50);
    [self.btnAction addTarget:self action:@selector(handleButtonPress:) forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:self.btnAction];

    self.lblStatus = [[UILabel alloc] initWithFrame:CGRectMake(100, 200, 200, 50)];
    self.lblStatus.text = @"Waiting...";
    [self.view addSubview:self.lblStatus];
}

- (void)setupEventHandlers {
    [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(processNotification:) name:@"ZXYNotification" object:nil];
}

- (void)handleButtonPress:(UIButton *)sender {
    [self executeComplexOperation];
}

- (void)processNotification:(NSNotification *)notification {
    [self updateStatusLabelWithInfo:notification.userInfo];
}

- (void)executeComplexOperation {
    // Perform some complex operation
    NSLog(@"Executing complex operation...");
}

- (void)updateStatusLabelWithInfo:(NSDictionary *)info {
    NSString *statusMessage = [NSString stringWithFormat:@"Status Updated: %@", info[@"status"]];
    self.lblStatus.text = statusMessage;
}

- (void)dealloc {
    [[NSNotificationCenter defaultCenter] removeObserver:self];
}

@end
  
