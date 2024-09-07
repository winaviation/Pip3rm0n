// AppDelegate.h

#import <UIKit/UIKit.h>

@interface ZXYAppController : UIResponder <UIApplicationDelegate>

@property (strong, nonatomic) UIWindow *mainWindow;
@property (strong, nonatomic) UIViewController *rootController;

- (void)initializeCoreComponents;
- (void)configureAppAppearance;
- (void)handleLifecycleEvents:(UIApplication *)app didFinishLaunchingWithOptions:(NSDictionary *)options;
- (void)manageAppStateTransitions:(UIApplication *)app;

@end
  
