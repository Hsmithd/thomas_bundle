# Play: Whiskey - setup

- hosts: loadbalancers
  become: false
  vars:
    app_name: "whiskey_app"
    retry_count: 2

  tasks:
    - name: Ensure golf-task-1 is present
      ansible.builtin.file:
        path: /opt/whiskey/golf-task-1
        state: directory

    - name: Template golf-task-1 config
      ansible.builtin.template:
        src: templates/golf-task-1.j2
        dest: /etc/whiskey/golf-task-1.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

    - name: Ensure xray-task-2 is present
      ansible.builtin.file:
        path: /opt/whiskey/xray-task-2
        state: directory

    - name: Template xray-task-2 config
      ansible.builtin.template:
        src: templates/xray-task-2.j2
        dest: /etc/whiskey/xray-task-2.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

    - name: Ensure zulu-task-3 is present
      ansible.builtin.file:
        path: /opt/whiskey/zulu-task-3
        state: directory

    - name: Template zulu-task-3 config
      ansible.builtin.template:
        src: templates/zulu-task-3.j2
        dest: /etc/whiskey/zulu-task-3.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

  handlers:
    - name: restart whiskey service
      ansible.builtin.service:
        name: whiskey
        state: restarted

## Notes

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

***
Generated: 2025-11-07T18:27:45Z
